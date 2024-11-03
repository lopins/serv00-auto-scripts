const fs = require('fs');
const puppeteer = require('puppeteer');
const axios = require('axios');

function formatToISO(date) {
    return date.toISOString().replace('T', ' ').replace('Z', '').replace(/\.\d{3}Z/, '');
}

async function delayTime(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function sendTelegramMessage(token, chatId, message) {
    const url = `https://api.telegram.org/bot${token}/sendMessage`;
    const data = {
        chat_id: chatId,
        text: message,
        reply_markup: {
            inline_keyboard: [
                [
                    {
                        text: '问题反馈❓',
                        url: 'https://t.me/lopinv'
                    }
                ]
            ]
        }
    };

    try {
        const response = await axios.post(url, data);
        console.log('消息已发送到 Telegram:', response.data);
    } catch (error) {
        console.error('发送 Telegram 消息时出错:', error.response ? error.response.data : error.message);
    }
}

(async () => {
    const accountsJson = fs.readFileSync('accounts.json', 'utf-8');
    const accounts = JSON.parse(accountsJson);
    const telegramToken = process.env.TELEGRAM_BOT_TOKEN;
    const telegramChatId = process.env.TELEGRAM_CHAT_ID;

    for (const account of accounts) {
        const { username, password, panel } = account;

        const browser = await puppeteer.launch({ headless: true });
        const page = await browser.newPage();

        let url = `https://${panel}/login/?next=/`;

        try {
            await page.goto(url);

            const usernameInput = await page.$('#id_username');
            if (usernameInput) {
                await usernameInput.click({ clickCount: 3 });
                await usernameInput.press('Backspace');
            }
            await page.type('#id_username', username);
            await page.type('#id_password', password);

            const loginButton = await page.$('#submit');
            if (loginButton) {
                await loginButton.click();
            } else {
                throw new Error('无法找到登录按钮');
            }

            await page.waitForNavigation();

            const isLoggedIn = await page.evaluate(() => {
                const logoutButton = document.querySelector('a[href="/logout/"]');
                return logoutButton !== null;
            });

            if (isLoggedIn) {
                const nowUtc = formatToISO(new Date());
                const nowBeijing = formatToISO(new Date(new Date().getTime() + 8 * 60 * 60 * 1000)); // 北京时间东8区
                console.log(`账号 ${username} 于北京时间 ${nowBeijing}（UTC时间 ${nowUtc}）登录成功！`);
                if (telegramToken && telegramChatId) {
                    await sendTelegramMessage(telegramToken, telegramChatId, `账号 ${username} 于北京时间 ${nowBeijing}（UTC时间 ${nowUtc}）登录成功！`);
                }
            } else {
                console.error(`账号 ${username} 登录失败，请检查账号和密码是否正确。`);
                if (telegramToken && telegramChatId) {
                    await sendTelegramMessage(telegramToken, telegramChatId, `账号 ${username} 登录失败，请检查账号和密码是否正确。`);
                }
            }
        } catch (error) {
            console.error(`账号 ${username} 登录时出现错误: ${error}`);
            if (telegramToken && telegramChatId) {
                await sendTelegramMessage(telegramToken, telegramChatId, `账号 ${username} 登录时出现错误: ${error.message}`);
            }
        } finally {
            await page.close();
            await browser.close();

            const delay = Math.floor(Math.random() * 8000) + 1000; // 随机延时1秒到8秒之间
            await delayTime(delay);
        }
    }
    console.log('所有账号登录完成！');
})();