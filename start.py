import keyboard
import time
import json
import os

class ActionHandler:
    def __init__(self):
        self.config = self.load_config()
        self.register_hotkeys()
    
    def load_config(self, filename="config.json"):
        if not os.path.exists(filename):
            default_config = {
                "writeconfig": {f"write{i}": None for i in range(9)},
                "pressconfig": {f"press{i}": None for i in range(9)},
                "holdconfig": {f"hold{i}": None for i in range(9)}
            }
            with open(filename, 'w') as f:
                json.dump(default_config, f, indent=4)
            return default_config
        
        with open(filename, 'r') as f:
            config = json.load(f)
            
            for config_type in ["writeconfig", "pressconfig", "holdconfig"]:
                if config_type not in config:
                    config[config_type] = {f"{config_type[:-6]}{i}": None for i in range(9)}
                else:
                    for i in range(9):
                        key = f"{config_type[:-6]}{i}"
                        if key not in config[config_type]:
                            config[config_type][key] = None
            
            return config
    
    def save_config(self, filename="config.json"):
        """Сохраняет текущую конфигурацию в файл"""
        with open(filename, 'w') as f:
            json.dump(self.config, f, indent=4)
    
    def register_hotkeys(self):
        for key, value in self.config['writeconfig'].items():
            if value and isinstance(value, list) and len(value) >= 2:
                try:
                    hotkey, text = value[:2]  
                    keyboard.add_hotkey(hotkey, self.write, args=(text,))
                    print(f"Зарегистрирован Write: {hotkey} -> '{text}'")
                except Exception as e:
                    print(f"Ошибка регистрации {key}: {e}")
        
        for key, value in self.config['pressconfig'].items():
            if value and isinstance(value, list) and len(value) >= 3:
                try:
                    hotkey, button, times = value[:3]  
                    
                    if isinstance(times, str) and times.isdigit():
                        times = int(times)
                    
                    delay = 0.1
                    if len(value) >= 4:
                        delay = value[3]
                        if isinstance(delay, str) and delay.replace('.', '', 1).isdigit():
                            delay = float(delay)
                    
                    keyboard.add_hotkey(hotkey, self.press, args=(button, times, delay))
                    print(f"Зарегистрирован Press: {hotkey} -> {button} ({times}x с задержкой {delay}s)")
                except Exception as e:
                    print(f"Ошибка регистрации {key}: {e}")
        
        for key, value in self.config['holdconfig'].items():
            if value and isinstance(value, list) and len(value) >= 3:
                try:
                    hotkey, button, holdtime = value[:3] 
                    
  
                    if isinstance(holdtime, str) and holdtime.replace('.', '', 1).isdigit():
                        holdtime = float(holdtime)
                    
                    keyboard.add_hotkey(hotkey, self.hold, args=(button, holdtime))
                    print(f"Зарегистрирован Hold: {hotkey} -> {button} ({holdtime}s)")
                except Exception as e:
                    print(f"Ошибка регистрации {key}: {e}")
    
    def press(self, button, times, delay):
        print(f"Выполняется Press: кнопка={button}, раз={times}, задержка={delay}s")
        for i in range(times):
            keyboard.press_and_release(button)
            time.sleep(delay)
    
    def hold(self, button, holdtime):
        print(f"Выполняется Hold: кнопка={button}, время={holdtime}s")
        keyboard.press(button)
        time.sleep(holdtime)
        keyboard.release(button)
    
    def write(self, text):
        print(f"Выполняется Write: текст='{text}'")
        keyboard.write(text)
    
    def update_config(self, action_type, slot, data):
        config_key = f"{action_type}config"
        slot_key = f"{action_type}{slot}"
        
        if config_key in self.config and slot_key in self.config[config_key]:

            if action_type == "write":

                self.config[config_key][slot_key] = data[:2]
            elif action_type == "press":

                press_data = data[:3]  
                if len(data) >= 4:
                    press_data.append(data[3])  
                self.config[config_key][slot_key] = press_data
            elif action_type == "hold":

                self.config[config_key][slot_key] = data[:3]
            else:
                print(f"Неизвестный тип действия: {action_type}")
                return False
            
            self.save_config()
            self.register_hotkeys()
            return True
        return False

def main():
    handler = ActionHandler()
    print("\nПрограмма запущена. Горячие клавиши зарегистрированы.")
    print("Нажмите Ctrl+C для выхода.\n")
    
    try:


        keyboard.wait()
    except KeyboardInterrupt:
        print("\nПрограмма завершена.")

if __name__ == "__main__":
    main()