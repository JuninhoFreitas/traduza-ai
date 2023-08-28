import os
from pathlib import Path
import pysubs2
from subsai import Tools

#@title Subtitles file
subtitles_file = './commongrace.srt'  #@param {type: "string"}
subs = pysubs2.load(subtitles_file)


Tools.available_translation_models()

#@title Select a Transaltion Model from the list above
translation_model = 'facebook/m2m100_1.2B'  #@param {type: "string"}

print(Tools.available_translation_languages(translation_model))

#@title Select languages from the list above
source_language = 'English'  #@param {type: "string"}
target_language = 'Portuguese'  #@param {type: "string"}

format = 'srt' #@param {type: "string"}
translated_file = f"{subtitles_file}-{source_language}-{target_language}.{format}"

translated_subs = Tools.translate(subs, source_language=source_language, target_language=target_language, model=translation_model)
translated_subs.save(translated_file)
print(f"translated file saved to {translated_file}")

