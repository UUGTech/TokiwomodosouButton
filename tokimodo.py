import serial
import keyboard
from playsound import playsound

sound = "./tokiwomodosou.mp3"

def main():
    ser = serial.Serial("COM5", 9600, timeout=0.1)
    while True:
        data = str(ser.readline().decode(encoding="utf-8"))
        if "Pressed" in data:
            keyboard.press("ctrl")
            keyboard.press_and_release("z")
            keyboard.release("ctrl")
            print("時を戻そう!")
            playsound(sound)
        
        if keyboard.is_pressed("esc"):
            ser.close()
            break


if __name__ == "__main__":
    main()