from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Rafeek=Client(
    "Auto Filter Bot",
    bot_token="bot token",
    api_id="api id",
    api_hash="api hash"
)

@Rafeek.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_text(
        text="๐ ๐ท๐ด๐ป๐พ {u.mention}\n\nโ ๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด ๐ธ๐ {message.chat.title}\n\n๐ต๏ธ ๐ธ ๐ฒ๐ฐ๐ฝ ๐ฟ๐๐พ๐๐ธ๐ณ๐ด ๐ผ๐พ๐๐ธ๐ด๐,\n\nโ ๐น๐๐๐ ๐ฐ๐ณ๐ณ ๐ผ๐ด ๐๐พ ๐๐พ๐๐ ๐ถ๐๐พ๐๐ฟ ๐ฐ๐ฝ๐ณ ๐ด๐ฝ๐น๐พ๐ ๐\n\n๐ฎโโ ๐ฒ๐๐ด๐ฐ๐๐พ๐ : <a href='https://t.me/Rafeeq_Kunnimon'>โ ๐๐๐๐๐ โ</a>",
        reply_markup=InlineKeyboardMarkup( [[
             InlineKeyboardButton('โ แดแดแด แดแด แดแด สแดแดส ษขสแดแดแดs โ', url='http://t.me/Movie_Roster_bot?startgroup=true')
            ],[
            InlineKeyboardButton('โจ แดกแดสแดษชษดษข ษขสแดแดแด โจ', url='https://t.me/MovieRosterGroup')
            ],[
            InlineKeyboardButton('๐ตโโ แดแดแด แดสแดแดแดส ๐ตโโ', url='https://t.me/Rafeeq_Kunnimon'),
            InlineKeyboardButton('โค๏ธ sแดแดแดแดสแด โค๏ธ', url='https://t.me/MovieRosterOfficial')
            ],[
            InlineKeyboardButton('๐ สแดสแด ๐', callback_data='help'),
            InlineKeyboardButton('๐ฐ แดสแดแดแด ๐ฐ', callback_data='about')
        ]]
            )
       )

@Rafeek.on_message(filters.command("help"))
async def start_message(bot, message):
    await message.reply_text(
        text="๐ สแดสสแดแดก {mention}\n\n}\nสแดสแด ษชแด แดสแด สแดสแด าแดส แดส\nแดแดแดแดแดษดแดแด.",
        reply_markup=InlineKeyboardMarkup( [[
             InlineKeyboardButton('๐ฎโโ แดแดแดษชษด ๐ฎโโ', callback_data='admin'),
            InlineKeyboardButton('๐ แดแดษดษดแดแดแด ๐', callback_data='coct'),
            ],[
            InlineKeyboardButton('๐ฅ๏ธ าษชสแดแดสs ๐ฅ๏ธ', callback_data='auto_manual'),      
            InlineKeyboardButton('๐จ๏ธ ษขแดสแดษดs ๐จ๏ธ', callback_data='gtrans'),
            ],[
            InlineKeyboardButton('โน๏ธ ษชษดาแด โน๏ธ', callback_data='info'),
            InlineKeyboardButton('๐งพ แดแดแดแดs ๐งพ', callback_data='memes'),
            ],[
            InlineKeyboardButton('๐ แดแดsแดแด ๐', callback_data='paste'),
            InlineKeyboardButton('๐ แดแดssแดกแดสแด ษขแดษด ๐', callback_data='genpassword'),
            ],[
            InlineKeyboardButton('๐ แดษชษด ๐', callback_data='pin'),
            InlineKeyboardButton('๐ง แดแดสษขแด ๐ง', callback_data='purge'),
            ],[
            InlineKeyboardButton('๐ฏ สแดsแดสษชแด ๐ฏ', callback_data='restric'),
            InlineKeyboardButton('๐ sแดแดสแดส ๐', callback_data='search'),
            ],[
            InlineKeyboardButton('โญ sสแดสแด แดแดxแด โญ', callback_data='sharetext'),
            InlineKeyboardButton('๐ถ แดแดsษชแด ๐ถ', callback_data='music'),
            ],[
            InlineKeyboardButton('๐ต แดแด-sแดแดแดแดส ๐ต', callback_data='tts'),
            InlineKeyboardButton('๐ แดษขสแดแดส ๐', callback_data='tgraph'),
            ],[
            InlineKeyboardButton('๐ธ แดแดxแด sสแดสแดษดแดส ๐น', callback_data='shortner'),
            InlineKeyboardButton('๐ง แดขแดแดสษชแดs ๐ง', callback_data='zombies'),
            ],[
            InlineKeyboardButton('โ๏ธ สแดแดแด โ๏ธ', callback_data='start')
        ]]
            )
       )

Rafeek.run()
