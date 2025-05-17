# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 20:01:07 2023

@author: LENOVO
"""
import tkinter as tk
import random

def read_words_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().splitlines()

def main_menu():
    def start_game():
        main_window.destroy()
        game_window(words)

    main_window = tk.Tk()
    main_window.title("主菜单")
    width = 500
    height = 100
    main_window.geometry(f"{width}x{height}")

    start_button = tk.Button(main_window,text="开始游戏", command=start_game)
    start_button.pack(padx=100,pady=20)

    main_window.mainloop()

def game_window(words):
   
    def select_next_word():
        total_words = len(words)
        weights = [1 / total_words] * total_words

        selected_word = random.choices(words, weights=weights)[0]
        return selected_word
    
    def shuffle_word(word):
        word_list = list(word)
        random.shuffle(word_list)
        return ''.join(word_list)

    def check_word():
        nonlocal consecutive_wrong_count

        entered_word = entry.get().strip()
        if entered_word == current_word:
            message_label.config(text="恭喜，你猜对了！", fg="green")
            consecutive_wrong_count = 0  
            next_word_button.config(state=tk.NORMAL)  
        else:
            message_label.config(text="你猜错了，请继续猜！", fg="red")
            consecutive_wrong_count += 1
            if consecutive_wrong_count >= max_wrong_count:
                with open("guess word.txt", "a") as file:
                    file.write(current_word + "\n")
                entry.config(state=tk.DISABLED)
                message_label.config(text="已经错误3次，请跳转下一个单词", fg="red")
                next_word_button.config(state=tk.NORMAL)

    def next_word():
        nonlocal current_word, shuffled_word, consecutive_wrong_count
        consecutive_wrong_count = 0  
        current_word = select_next_word()
        shuffled_word = shuffle_word(current_word)
        word_label.config(text=shuffled_word)
        entry.config(state=tk.NORMAL)
        entry.delete(0, "end")
        message_label.config(text="")
        next_word_button.config(state=tk.DISABLED)  

    game_window = tk.Tk()
    game_window.title("猜单词游戏")
    game_window.geometry("500x400")

    current_word = select_next_word()
    shuffled_word = shuffle_word(current_word)
    consecutive_wrong_count = 0 
    max_wrong_count = 3  

    word_label = tk.Label(game_window, text=shuffled_word, font=("Arial", 18))
    word_label.pack(padx=100,pady=20)

    entry = tk.Entry(game_window, width=30)
    entry.pack(pady=10)

    check_button = tk.Button(game_window, text="确认", command=check_word)
    check_button.pack(pady=10)

    next_word_button = tk.Button(game_window, text="下一个单词", command=next_word, state=tk.DISABLED)
    next_word_button.pack(pady=10)

    message_label = tk.Label(game_window, text="")
    message_label.pack(pady=10)

    game_window.mainloop()

word_file_path = "guess word.txt"
words = read_words_from_file(word_file_path)

main_menu()

