#//uiuiuiu
import time

def typing_speed_test():
    print("Welcome to Typing Speed Test!")
    input("Press Enter when you are ready to start...")
    start_time = time.time()
    prompt = "The quick brown fox jumps over the lazy dog."
    print("Type the following text:")
    print(prompt)
    user_input = input()
    end_time = time.time()
    elapsed_time = end_time - start_time

    correct_characters = 0
    for i in range(min(len(prompt), len(user_input))):
        if prompt[i] == user_input[i]:
            correct_characters += 1

    accuracy = correct_characters / len(prompt) * 100
    words_per_minute = len(user_input.split()) / (elapsed_time / 60)

    print("\nTest Results:")
    print("Time elapsed: {:.2f} seconds".format(elapsed_time))
    print("Accuracy: {:.2f}%".format(accuracy))
    print("Words per minute: {:.2f}".format(words_per_minute))

if __name__ == "__main__":
    typing_speed_test()

