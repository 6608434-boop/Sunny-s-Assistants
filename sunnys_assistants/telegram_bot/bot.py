"""
Main Telegram bot module.
Initializes the bot and starts polling.
"""

import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# Временные заглушки для handlers (пока бот не работает с реальными use cases)
async def start(update, context):
    """Обработчик команды /start"""
    await update.message.reply_text(
        "👋 Добро пожаловать в Sunny's Assistants!\n\n"
        "Бот находится в режиме разработки. Скоро здесь будет магия."
    )


async def help_command(update, context):
    """Обработчик команды /help"""
    await update.message.reply_text(
        "Доступные команды:\n"
        "/start - Начало работы\n"
        "/help - Эта справка"
    )


async def echo(update, context):
    """Заглушка для текстовых сообщений"""
    await update.message.reply_text(
        "Я пока только учусь. Попробуй /help"
    )


def main():
    """Запуск бота"""
    # Создаём приложение
    application = Application.builder().token("YOUR_TOKEN_HERE").build()

    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Запускаем бота
    logger.info("Бот запущен и готов к работе")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()