from os import listdir, mkdir
from pyrogram import Client
from Faz import config
from Faz.tgcalls.queues import clear, get, is_empty, put, task_done
from Faz.tgcalls import queues
from Faz.tgcalls.youtube import download
from Faz.tgcalls.calls import run, pytgcalls
from Faz.tgcalls.calls import client

if "raw_files" not in listdir():
    mkdir("raw_files")

from Faz.tgcalls.convert import convert
