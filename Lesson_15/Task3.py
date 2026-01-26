
class TVController:
 
    def __init__(self, channels):
        self.channels = channels
        self.current_channel_index = 0 # Початковий канал - перший у списку (індекс 0)

    def first_channel(self):   #Вмикає перший канал зі списку
        self.current_channel_index = 0
        return self.channels[self.current_channel_index]

    def last_channel(self): #Вмикає останній канал зі списк
        self.current_channel_index = len(self.channels) - 1
        return self.channels[self.current_channel_index]

    def turn_channel(self, n): #Вмикає канал за його номером
        channel_index = n - 1
        if 0 <= channel_index < len(self.channels):
            self.current_channel_index = channel_index
            return self.channels[self.current_channel_index]
        
    def next_channel(self):   #Вмикає наступний канал. Якщо поточний - останній, вмикає перший
        self.current_channel_index = (self.current_channel_index + 1) % len(self.channels)
        return self.channels[self.current_channel_index]

    def previous_channel(self):    #Вмикає попередній канал. Якщо поточний - перший, вмикає останній
        self.current_channel_index = (self.current_channel_index - 1 + len(self.channels)) % len(self.channels)
        return self.channels[self.current_channel_index]

    def current_channel(self):   #Повертає назву поточного увімкненого каналу
        return self.channels[self.current_channel_index]

    def exists(self, identifier):   #Перевіряє, чи існує канал за номером або назвою
        if isinstance(identifier, int):
            # Перевірка за номером (нумерація з 1)
            # Перевіряємо, чи входить індекс (identifier - 1) у допустимий діапазон
            is_found = 0 <= identifier - 1 < len(self.channels)
        elif isinstance(identifier, str):
            # Перевірка за назвою
            # Просто перевіряємо, чи є назва у списку каналів
            is_found = identifier in self.channels
        else:
            is_found = False  # Якщо тип аргументу не підтримується
            
        return "Yes" if is_found else "No"

CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)

print(f"Початковий канал: {controller.current_channel()}") 

print(f"first_channel(): {controller.first_channel()}")
print(f"last_channel(): {controller.last_channel()}")
print(f"turn_channel(1): {controller.turn_channel(1)}")
print(f"next_channel(): {controller.next_channel()}")
print(f"previous_channel(): {controller.previous_channel()}")
print(f"current_channel(): {controller.current_channel()}")
print(f"exists(4): {controller.exists(4)}")
print(f"exists('BBC'): {controller.exists('BBC')}")
print(f"exists('CNN'): {controller.exists('CNN')}")

