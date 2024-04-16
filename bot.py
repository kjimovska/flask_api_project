# import telebot
# from config import TELEGRAM_BOT_TOKEN
# from flask import jsonify
# import requests

# bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN, parse_mode=None)

# def start_bot_polling():
#     try:
#         bot.polling(none_stop=True)
#     except Exception as e:
#         print(f"Polling bot failed: {e}")


# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, "Hey there! Use /average_spending to get average spending by age.")

# @bot.message_handler(commands=['average_spending'])
# def send_average_spending(message):
#     url = "http://127.0.0.1:5000/average_spending_by_age"
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  
#         data = response.json()
        
#         message_lines = ["Average Spending by Age-Ranges:"]
#         for age_range, avg_spending in data.items():
#             line = f"{age_range}: ${avg_spending:.2f}"
#             message_lines.append(line)
#         final_message = "\n".join(message_lines)
        
#         # prakjanje na porakata(average spending) preku Telegram bot, i setiranje Exceptions
#         bot.send_message(message.chat.id, final_message)
#     except requests.exceptions.HTTPError as http_err:
#         print(f"HTTP error occurred: {http_err}")
#         bot.reply_to(message, f"HTTP error occurred: {http_err}")
#     except Exception as e:
#         print(f"Other error occurred: {e}")
#         bot.reply_to(message, f"An error occurred while processing your request: {str(e)}")


# if __name__ == "__main__":
#     start_bot_polling()