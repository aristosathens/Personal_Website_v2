# Aristos Athens

'''
    Captcha generator
'''

import atexit

import os
import string
from random import choice, choices
from PIL import Image, ImageDraw

class _captcha:
    '''
        Store data for single captcha.
    '''

    def __init__(self, code, answer, file_name):
        '''
            Init _captcha object.
        '''
        self._code = code
        self._answer = answer
        self._file_name = file_name

    def clean(self):
        '''
            Delete the file associated with this captcha.
        '''
        print("In _captcha __del__")
        os.remove(self._file_name)

    def matches(self, answer):
        '''
            Check if the answer matches.
        '''
        return self._answer == answer


class Captcha:
    '''
        Generate and store _captchas.
        Static class.
    '''
    _code_length = 20
    _text_offset = 10
    _generate_captchas = {}
    _num_generated = 0
    _folder = "static/"

    @staticmethod
    def init_clean():
        '''
            Finds captcha image files and deletes them.
            Image file_names are "captcha_<number>.png".
        '''
        print("IN INIT CLEAN.")
        for file in os.listdir():
            if file.startswith("captcha_") and file.endswith(".png"):
                os.remove(file)

    @staticmethod
    def clean():
        '''
            Clean all of the _captchas stored in this object.
        '''
        for _, c in Captcha._generate_captchas.items():
            c.clean()

    @staticmethod
    def generate_captcha(size = (300, 200), length = 5):
        '''
            Generate a new captcha.
            Return (code, file_name).
        '''
        # Generate captcha info
        while True:
            code = ''.join(choices(string.ascii_uppercase + string.digits, k = Captcha._code_length))
            if code not in Captcha._generate_captchas:
                break
        answer = ''.join(choices(string.ascii_uppercase + string.digits, k = length))
        file_name = Captcha._folder + "captcha_" + str(Captcha._num_generated) + ".png"
        Captcha._num_generated += 1

        # Create image. Draw answer onto image. Save image.
        image = Image.new('RGB', size, color = 'red')
        d = ImageDraw.Draw(image)
        text_location = (choice(range(Captcha._text_offset, size[0] - Captcha._text_offset)), \
                         choice(range(Captcha._text_offset, size[1] - Captcha._text_offset)))
        d.text(text_location, answer, fill=(255,255,0))
        image.save(file_name)

        # Store data in _captcha object
        Captcha._generate_captchas[code] = _captcha(code, answer,  file_name)
        print(Captcha._generate_captchas)
        print(answer)

        return (code, file_name)

    @staticmethod
    def check_answer(code, answer):
        '''
            Check if answer matches. If it does not, it deletes the captcha.
        '''
        if code not in Captcha._generate_captchas:
            raise Exception("There is not captcha matching code: " + str(code))
        correct = Captcha._generate_captchas[code].matches(answer)

        # Delete captcha object and image file.
        Captcha._generate_captchas[code].clean()
        del Captcha._generate_captchas[code]

        return correct


def _clean_up():
    '''
        When interpreter exits, call Captcha.clean() to delete leftover captcha image files, if any.
        Note, this is not 100% guaranteed to get called! 
    '''
    Captcha.clean()
    

'''
    Code to run when module is loaded.
'''
Captcha.init_clean()


'''
    Code to run when process exits.
'''
atexit.register(_clean_up)
