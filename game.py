import sys
from dataclasses import dataclass, field

import pygame


WIDTH = 960
HEIGHT = 640
FPS = 60

SKY = (29, 32, 45)
INK = (12, 13, 18)
WHITE = (238, 238, 232)
MINT = (109, 224, 172)
GOLD = (247, 194, 72)
RED = (238, 82, 83)
BLUE = (89, 164, 255)
PURPLE = (160, 120, 255)
STONE = (88, 93, 108)
STONE_DARK = (52, 56, 70)
PINK = (255, 103, 158)
BLACK = (6, 7, 11)
BONE = (246, 239, 217)
STONE_LIGHT = (120, 126, 142)
WOOD = (118, 75, 45)
WOOD_DARK = (62, 38, 28)
SKY_LIGHT = (45, 50, 70)
SKY_DARK = (21, 24, 36)

GRAVITY = 1900
MOVE_SPEED = 310
JUMP_SPEED = 690
JUMP_BUFFER_TIME = 0.12
COYOTE_TIME = 0.1

RESOLUTIONS = [(960, 640), (1280, 720), (1920, 1080)]

DEFAULT_KEYS = {
    "jump": pygame.K_SPACE,
    "left": pygame.K_LEFT,
    "right": pygame.K_RIGHT,
    "reset": pygame.K_r,
    "pause": pygame.K_ESCAPE,
}


LANGUAGES = {
    "рус": {
        "title": "INFINITE TROLL",
        "subtitle": "THE GAME",
        "play": "Играть",
        "settings": "Настройки",
        "exit": "Выход",
        "exit_ui": "Выход",
        "lang": "Язык",
        "hold_jump": "Зажатие прыжка",
        "hold_jump_on": "Вкл",
        "hold_jump_off": "Выкл",
        "textures": "Текстуры",
        "tx_classic": "Классика",
        "tx_dark": "Тьма",
        "tx_warm": "Тепло",
        "tx_neon": "Неон",
        "back": "Назад",
        "deaths": "Смерти",
        "room": "Комната",
        "finish_title": "ТЫ ВЫБРАЛСЯ",
        "finish_stats": "Смертей всего",
        "finish_again": "Нажми ENTER, чтобы начать страдать заново",
        "finish_esc": "ESC - меню",
        "toast_intro": "Чистая оригинальная игра. Только нечестные маленькие сюрпризы.",
        "die_fall": "Пол подал жалобу.",
        "die_spike": "Ловушка терпеливо ждала.",
        "die_fake": "Не та дверь. Зато красивая.",
        "die_manual": "Ручной перезапуск. Стильно.",
        "finish_toast": "Ты выбрался и почти ничему не научился.",
        "menu_pause": "Пауза",
        "resume": "Продолжить",
        "controls": "Управление",
        "resolution": "Разрешение",
        "jump_key": "Прыжок",
        "left_key": "Влево",
        "right_key": "Вправо",
        "reset_key": "Сброс",
        "press_key": "Нажми клавишу...",
    },
    "қаз": {
        "title": "INFINITE TROLL",
        "subtitle": "THE GAME",
        "play": "Ойнау",
        "settings": "Баптаулар",
        "exit": "Шығу",
        "exit_ui": "Шығу",
        "lang": "Тіл",
        "hold_jump": "Секіруді ұстау",
        "hold_jump_on": "Қосу",
        "hold_jump_off": "Өшіру",
        "textures": "Текстуралар",
        "tx_classic": "Классика",
        "tx_dark": "Қараңғы",
        "tx_warm": "Жылы",
        "tx_neon": "Неон",
        "back": "Артқа",
        "deaths": "Өлім",
        "room": "Бөлме",
        "finish_title": "СЕН ШЫҚТЫҢ",
        "finish_stats": "Барлық өлім",
        "finish_again": "ENTER - қайта азап шегу",
        "finish_esc": "ESC - мәзір",
        "toast_intro": "Таза түпнұсқа ойын. Тек кішкентай тосын сыйлар.",
        "die_fall": "Еден шағымданды.",
        "die_spike": "Қақпан күтті.",
        "die_fake": "Дұрыс емес есік. Бірақ әдемі.",
        "die_manual": "Қолмен қосу. Стильді.",
        "finish_toast": "Сен шықтың және ештеңе үйренбедің.",
        "menu_pause": "Үзіліс",
        "resume": "Жалғастыру",
        "controls": "Баптау",
        "resolution": "Рұқсат",
        "jump_key": "Секіру",
        "left_key": "Солға",
        "right_key": "Оңға",
        "reset_key": "Қайта бастау",
        "press_key": "Пернені басыңыз...",
    },
    "eng": {
        "title": "INFINITE TROLL",
        "subtitle": "THE GAME",
        "play": "Play",
        "settings": "Settings",
        "exit": "Exit",
        "exit_ui": "Exit",
        "lang": "Language",
        "hold_jump": "Hold Jump",
        "hold_jump_on": "On",
        "hold_jump_off": "Off",
        "textures": "Textures",
        "tx_classic": "Classic",
        "tx_dark": "Dark",
        "tx_warm": "Warm",
        "tx_neon": "Neon",
        "deaths": "Deaths",
        "room": "Room",
        "finish_title": "YOU ESCAPED",
        "finish_stats": "Total Deaths",
        "finish_again": "Press ENTER to suffer again",
        "finish_esc": "ESC - menu",
        "toast_intro": "A pure original game. Only unfair little surprises.",
        "die_fall": "The floor filed a complaint.",
        "die_spike": "The trap waited patiently.",
        "die_fake": "Wrong door. Pretty though.",
        "die_manual": "Manual restart. Stylish.",
        "finish_toast": "You escaped and learned almost nothing.",
        "menu_pause": "Pause",
        "resume": "Resume",
        "controls": "Controls",
        "back": "Back",
        "resolution": "Resolution",
        "jump_key": "Jump",
        "left_key": "Left",
        "right_key": "Right",
        "reset_key": "Reset",
        "press_key": "Press a key...",
    },
}

TEXTURE_SETS = {
    "classic": {
        "brick": ("brick", (88, 93, 108), (52, 56, 70), (89, 164, 255)),
        "vanish": ("vanish", (72, 143, 196)),
        "wall": ("wall", (29, 32, 45), (45, 50, 70), (21, 24, 36)),
    },
    "dark": {
        "brick": ("brick", (35, 35, 45), (20, 20, 30), (60, 55, 70)),
        "vanish": ("vanish", (20, 50, 80)),
        "wall": ("wall", (10, 8, 18), (22, 18, 30), (6, 5, 12)),
    },
    "warm": {
        "brick": ("brick", (160, 100, 60), (120, 70, 40), (200, 150, 100)),
        "vanish": ("vanish", (200, 120, 60)),
        "wall": ("wall", (50, 30, 15), (70, 45, 25), (35, 20, 10)),
    },
    "neon": {
        "brick": ("brick", (20, 20, 50), (10, 10, 35), (60, 40, 100)),
        "vanish": ("vanish", (80, 10, 120)),
        "wall": ("wall", (5, 5, 25), (15, 10, 40), (2, 2, 15)),
    },
}


def build_textures(set_name):
    data = TEXTURE_SETS[set_name]
    textures = {}
    brick_data = data["brick"]
    tex = pygame.Surface((48, 48)).convert()
    tex.fill(brick_data[1])
    for y in range(0, 48, 12):
        stagger = 24 if (y // 12) % 2 else 0
        pygame.draw.line(tex, brick_data[2], (0, y), (48, y), 2)
        for x in range(-stagger, 49, 24):
            pygame.draw.line(tex, brick_data[2], (x, y), (x, y + 12), 2)
    for dot in ((9, 8), (34, 18), (18, 35), (42, 40)):
        pygame.draw.circle(tex, brick_data[3], dot, 1)
    textures["brick"] = tex

    vanish_data = data["vanish"]
    tex2 = pygame.Surface((48, 48)).convert()
    tex2.fill(vanish_data[1])
    for x in range(0, 48, 8):
        lighter = tuple(min(c + 40, 255) for c in vanish_data[1])
        darker = tuple(max(c - 20, 0) for c in vanish_data[1])
        pygame.draw.line(tex2, lighter, (x, 0), (x + 24, 48), 2)
    pygame.draw.rect(tex2, darker, tex2.get_rect(), 2)
    textures["vanish"] = tex2

    wall_data = data["wall"]
    tex3 = pygame.Surface((64, 64)).convert()
    tex3.fill(wall_data[1])
    for y in range(0, 64, 16):
        for x in range(0, 64, 16):
            shade = wall_data[2] if (x // 16 + y // 16) % 2 == 0 else wall_data[3]
            pygame.draw.rect(tex3, shade, pygame.Rect(x, y, 16, 16), 1)
    textures["wall"] = tex3
    return textures


class Button:
    def __init__(self, rect, text, color=STONE, hover_color=STONE_LIGHT, text_color=WHITE):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.hovered = False

    def draw(self, screen, font):
        color = self.hover_color if self.hovered else self.color
        pygame.draw.rect(screen, color, self.rect, border_radius=6)
        pygame.draw.rect(screen, WHITE, self.rect, 2, border_radius=6)
        label = font.render(self.text, True, self.text_color)
        screen.blit(label, label.get_rect(center=self.rect.center))

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False


@dataclass
class Platform:
    rect: pygame.Rect
    color: tuple = STONE
    hidden_until_step: int = -1
    vanish_on_touch: bool = False
    touched: bool = False


@dataclass
class Spike:
    rect: pygame.Rect
    hidden_until_step: int = -1
    active: bool = True


@dataclass
class MessageZone:
    rect: pygame.Rect
    text: str
    once: bool = False
    shown: bool = False


@dataclass
class FallingObstacle:
    rect: pygame.Rect
    start_y: int
    trigger_x: int | float = 0
    speed: float = 300.0
    active: bool = False
    landed: bool = False
    current_y: float = 0.0
    is_spike: bool = True


@dataclass
class Level:
    name: str
    spawn: tuple
    platforms: list
    spikes: list
    messages: list
    door: pygame.Rect
    fake_door: pygame.Rect | None = None
    reveal_points: tuple = field(default_factory=lambda: (220, 280, 340, 400, 460, 520))
    falling: list = field(default_factory=list)


class Player:
    def __init__(self, spawn):
        self.rect = pygame.Rect(spawn[0], spawn[1], 32, 42)
        self.vel = pygame.Vector2(0, 0)
        self.on_ground = False
        self.coyote_timer = 0.0
        self.jump_buffer = 0.0
        self.spawn = spawn

    def reset(self, spawn=None):
        if spawn is not None:
            self.spawn = spawn
        self.rect.topleft = self.spawn
        self.vel.update(0, 0)
        self.on_ground = False
        self.coyote_timer = 0.0
        self.jump_buffer = 0.0


class Menu:
    def __init__(self, game):
        self.game = game
        self.state = "main"
        self.buttons = {}
        self.rebinding = None
        self.build_buttons()

    def tr(self, key):
        return LANGUAGES[self.game.lang].get(key, key)

    def key_name(self, key):
        names = {
            pygame.K_SPACE: "SPACE", pygame.K_LEFT: "LEFT", pygame.K_RIGHT: "RIGHT",
            pygame.K_UP: "UP", pygame.K_DOWN: "DOWN", pygame.K_RETURN: "ENTER",
            pygame.K_ESCAPE: "ESC", pygame.K_TAB: "TAB", pygame.K_LSHIFT: "LSHIFT",
            pygame.K_RSHIFT: "RSHIFT", pygame.K_LCTRL: "LCTRL", pygame.K_RCTRL: "RCTRL",
            pygame.K_a: "A", pygame.K_b: "B", pygame.K_c: "C", pygame.K_d: "D",
            pygame.K_e: "E", pygame.K_f: "F", pygame.K_g: "G", pygame.K_h: "H",
            pygame.K_i: "I", pygame.K_j: "J", pygame.K_k: "K", pygame.K_l: "L",
            pygame.K_m: "M", pygame.K_n: "N", pygame.K_o: "O", pygame.K_p: "P",
            pygame.K_q: "Q", pygame.K_r: "R", pygame.K_s: "S", pygame.K_t: "T",
            pygame.K_u: "U", pygame.K_v: "V", pygame.K_w: "W", pygame.K_x: "X",
            pygame.K_y: "Y", pygame.K_z: "Z",
        }
        return names.get(key, pygame.key.name(key).upper())

    def build_buttons(self):
        bw, bh = 340, 42
        cx = WIDTH // 2 - bw // 2
        ys = [170, 222, 274, 326, 378, 430]
        self.buttons = {
            "main": [
                Button((cx, 260, bw, bh), self.tr("play"), STONE, STONE_LIGHT),
                Button((cx, 325, bw, bh), self.tr("settings"), STONE, STONE_LIGHT),
                Button((cx, 390, bw, bh), self.tr("exit_ui"), STONE, STONE_LIGHT),
            ],
            "settings": [
                Button((cx, ys[0], bw, bh), "", STONE, STONE_LIGHT),
                Button((cx, ys[1], bw, bh), "", STONE, STONE_LIGHT),
                Button((cx, ys[2], bw, bh), "", STONE, STONE_LIGHT),
                Button((cx, ys[3], bw, bh), "", STONE, STONE_LIGHT),
                Button((cx, ys[4], bw, bh), "", STONE, STONE_LIGHT),
                Button((cx, ys[5], bw, bh), self.tr("back"), STONE, STONE_LIGHT),
            ],
            "paused": [
                Button((cx, 260, bw, bh), self.tr("resume"), STONE, STONE_LIGHT),
                Button((cx, 325, bw, bh), self.tr("settings"), STONE, STONE_LIGHT),
                Button((cx, 390, bw, bh), self.tr("exit_ui"), STONE, STONE_LIGHT),
            ],
            "controls": [
                Button((cx, ys[0], bw, bh), "", STONE, STONE_LIGHT),
                Button((cx, ys[1], bw, bh), "", STONE, STONE_LIGHT),
                Button((cx, ys[2], bw, bh), "", STONE, STONE_LIGHT),
                Button((cx, ys[3], bw, bh), "", STONE, STONE_LIGHT),
                Button((cx, ys[4], bw, bh), self.tr("back"), STONE, STONE_LIGHT),
            ],
        }

    def refresh_texts(self):
        self.buttons["main"][0].text = self.tr("play")
        self.buttons["main"][1].text = self.tr("settings")
        self.buttons["main"][2].text = self.tr("exit_ui")
        self.buttons["settings"][5].text = self.tr("back")
        self.buttons["paused"][0].text = self.tr("resume")
        self.buttons["paused"][1].text = self.tr("settings")
        self.buttons["paused"][2].text = self.tr("exit_ui")
        self.buttons["controls"][4].text = self.tr("back")
        self.update_settings_labels()
        self.update_controls_labels()

    def update_settings_labels(self):
        lang_names = {"рус": "Русский", "қаз": "Қазақша", "eng": "English"}
        hold = self.tr("hold_jump_on") if self.game.hold_jump else self.tr("hold_jump_off")
        tx_names = {"classic": self.tr("tx_classic"), "dark": self.tr("tx_dark"), "warm": self.tr("tx_warm"), "neon": self.tr("tx_neon")}
        w, h = RESOLUTIONS[self.game.res_index]
        res = f"{w}x{h}"
        self.buttons["settings"][0].text = f"{self.tr('lang')}: {lang_names[self.game.lang]}"
        self.buttons["settings"][1].text = f"{self.tr('hold_jump')}: {hold}"
        self.buttons["settings"][2].text = f"{self.tr('textures')}: {tx_names[self.game.texture_set]}"
        self.buttons["settings"][3].text = f"{self.tr('resolution')}: {res}"
        self.buttons["settings"][4].text = self.tr("controls")

    def update_controls_labels(self):
        b = self.game.key_bindings
        self.buttons["controls"][0].text = f"{self.tr('jump_key')}: {self.key_name(b['jump'])}"
        self.buttons["controls"][1].text = f"{self.tr('left_key')}: {self.key_name(b['left'])}"
        self.buttons["controls"][2].text = f"{self.tr('right_key')}: {self.key_name(b['right'])}"
        self.buttons["controls"][3].text = f"{self.tr('reset_key')}: {self.key_name(b['reset'])}"

    def handle_event(self, event):
        if self.rebinding:
            if event.type == pygame.KEYDOWN:
                self.game.key_bindings[self.rebinding] = event.key
                self.rebinding = None
                self.update_controls_labels()
                return True
            return False

        btns = self.buttons.get(self.state, [])
        for i, btn in enumerate(btns):
            if btn.handle_event(event):
                if self.state == "main":
                    if i == 0:
                        self.game.start_game()
                    elif i == 1:
                        self.state = "settings"
                        self.update_settings_labels()
                    elif i == 2:
                        self.game.running = False
                elif self.state == "settings":
                    if i == 0:
                        langs = ["рус", "қаз", "eng"]
                        idx = (langs.index(self.game.lang) + 1) % len(langs)
                        self.game.lang = langs[idx]
                        self.game.load_textures()
                        self.refresh_texts()
                    elif i == 1:
                        self.game.hold_jump = not self.game.hold_jump
                        self.update_settings_labels()
                    elif i == 2:
                        txs = ["classic", "dark", "warm", "neon"]
                        idx = (txs.index(self.game.texture_set) + 1) % len(txs)
                        self.game.texture_set = txs[idx]
                        self.game.load_textures()
                        self.update_settings_labels()
                    elif i == 3:
                        self.game.cycle_resolution()
                        self.update_settings_labels()
                    elif i == 4:
                        self.state = "controls"
                        self.update_controls_labels()
                    elif i == 5:
                        self.state = "paused" if self.game.playing else "main"
                elif self.state == "paused":
                    if i == 0:
                        self.game.playing = True
                    elif i == 1:
                        self.state = "settings"
                        self.update_settings_labels()
                    elif i == 2:
                        self.game.running = False
                elif self.state == "controls":
                    if i == 0:
                        self.rebinding = "jump"
                        self.buttons["controls"][0].text = self.tr("press_key")
                    elif i == 1:
                        self.rebinding = "left"
                        self.buttons["controls"][1].text = self.tr("press_key")
                    elif i == 2:
                        self.rebinding = "right"
                        self.buttons["controls"][2].text = self.tr("press_key")
                    elif i == 3:
                        self.rebinding = "reset"
                        self.buttons["controls"][3].text = self.tr("press_key")
                    elif i == 4:
                        self.state = "settings"
                        self.update_settings_labels()
                return True
        return False


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Infinite Troll")
        self.internal = pygame.Surface((960, 640))
        self.window = pygame.display.set_mode((960, 640))
        self.screen = self.internal
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("consolas", 22)
        self.small = pygame.font.SysFont("consolas", 16)
        self.big = pygame.font.SysFont("consolas", 42, bold=True)
        self.title_font = pygame.font.SysFont("consolas", 32, bold=True)
        self.menu_font = pygame.font.SysFont("consolas", 22, bold=True)

        self.lang = "рус"
        self.hold_jump = False
        self.texture_set = "classic"
        self.key_bindings = dict(DEFAULT_KEYS)
        self.res_index = 0
        self.playing = False
        self.textures = build_textures(self.texture_set)

        self.levels = self.build_levels()
        self.level_index = 0
        self.level = self.levels[self.level_index]
        self.player = Player(self.level.spawn)
        self.deaths = 0
        self.reveal_stage = 0
        self.max_player_x = self.player.rect.centerx
        self.falling_obstacles: list[FallingObstacle] = []
        self.toast = ""
        self.toast_timer = 0
        self.camera_shake = 0
        self.finished = False
        self.running = True

        self.menu = Menu(self)

    def tr(self, key):
        return LANGUAGES[self.lang].get(key, key)

    def load_textures(self):
        self.textures = build_textures(self.texture_set)

    def cycle_resolution(self):
        self.res_index = (self.res_index + 1) % len(RESOLUTIONS)
        w, h = RESOLUTIONS[self.res_index]
        self.window = pygame.display.set_mode((w, h))
        self.menu.build_buttons()
        self.menu.refresh_texts()

    def build_levels(self):
        return [
            Level(
                name="Комната 1: Первый шаг",
                spawn=(60, 505),
                platforms=[
                    Platform(pygame.Rect(0, 585, 960, 55)),
                    Platform(pygame.Rect(120, 510, 180, 24)),
                    Platform(pygame.Rect(380, 450, 150, 24)),
                    Platform(pygame.Rect(620, 390, 150, 24)),
                    Platform(pygame.Rect(840, 490, 100, 24)),
                ],
                spikes=[],
                messages=[
                    MessageZone(pygame.Rect(80, 470, 140, 80), "Добро пожаловать. Тут всё просто. Пока что.", True),
                ],
                door=pygame.Rect(700, 324, 42, 66),
                fake_door=pygame.Rect(860, 424, 42, 66),
            ),
            Level(
                name="Комната 2: Исчезающий путь",
                spawn=(55, 505),
                platforms=[
                    Platform(pygame.Rect(0, 585, 960, 55)),
                    Platform(pygame.Rect(100, 510, 110, 24), vanish_on_touch=True),
                    Platform(pygame.Rect(260, 510, 110, 24), vanish_on_touch=True),
                    Platform(pygame.Rect(420, 510, 110, 24), vanish_on_touch=True),
                    Platform(pygame.Rect(580, 510, 110, 24), vanish_on_touch=True),
                    Platform(pygame.Rect(740, 450, 120, 24)),
                    Platform(pygame.Rect(830, 520, 110, 24)),
                ],
                spikes=[
                    Spike(pygame.Rect(200, 552, 55, 33)),
                    Spike(pygame.Rect(360, 552, 55, 33)),
                    Spike(pygame.Rect(520, 552, 55, 33)),
                ],
                messages=[
                    MessageZone(pygame.Rect(80, 460, 140, 90), "Платформы исчезают, когда на них наступаешь. Беги.", True),
                ],
                door=pygame.Rect(865, 454, 42, 66),
                fake_door=pygame.Rect(750, 384, 42, 66),
            ),
            Level(
                name="Комната 3: Сверху опасно",
                spawn=(60, 505),
                platforms=[
                    Platform(pygame.Rect(0, 585, 960, 55)),
                    Platform(pygame.Rect(80, 510, 160, 24)),
                    Platform(pygame.Rect(300, 460, 130, 24)),
                    Platform(pygame.Rect(500, 405, 130, 24)),
                    Platform(pygame.Rect(700, 340, 160, 24)),
                    Platform(pygame.Rect(810, 495, 95, 24)),
                ],
                spikes=[],
                messages=[
                    MessageZone(pygame.Rect(60, 460, 140, 90), "Шипы падают сверху. Не стой под ними.", True),
                ],
                door=pygame.Rect(845, 274, 42, 66),
                fake_door=pygame.Rect(730, 300, 42, 66),
                falling=[
                    FallingObstacle(pygame.Rect(240, 552, 70, 33), start_y=72, trigger_x=240, speed=300),
                    FallingObstacle(pygame.Rect(420, 552, 70, 33), start_y=72, trigger_x=420, speed=300),
                    FallingObstacle(pygame.Rect(580, 552, 70, 33), start_y=72, trigger_x=580, speed=300),
                ],
            ),
            Level(
                name="Комната 4: Лживые таблички",
                spawn=(55, 505),
                platforms=[
                    Platform(pygame.Rect(0, 585, 960, 55)),
                    Platform(pygame.Rect(150, 510, 120, 24)),
                    Platform(pygame.Rect(350, 440, 80, 24)),
                    Platform(pygame.Rect(520, 370, 100, 24)),
                    Platform(pygame.Rect(710, 300, 100, 24)),
                    Platform(pygame.Rect(800, 500, 95, 24)),
                ],
                spikes=[
                    Spike(pygame.Rect(265, 552, 70, 33)),
                    Spike(pygame.Rect(470, 552, 70, 33)),
                ],
                messages=[
                    MessageZone(pygame.Rect(120, 460, 100, 70), "Прыгай! (тут правда безопасно)", True),
                    MessageZone(pygame.Rect(480, 320, 100, 70), "Не прыгай! (ну пожалуйста)", True),
                ],
                door=pygame.Rect(845, 234, 42, 66),
                fake_door=pygame.Rect(820, 434, 42, 66),
            ),
            Level(
                name="Комната 5: Шипы из ниоткуда",
                spawn=(60, 505),
                platforms=[
                    Platform(pygame.Rect(0, 585, 960, 55)),
                    Platform(pygame.Rect(140, 510, 120, 24)),
                    Platform(pygame.Rect(320, 460, 110, 24)),
                    Platform(pygame.Rect(490, 400, 110, 24)),
                    Platform(pygame.Rect(640, 340, 110, 24)),
                    Platform(pygame.Rect(800, 490, 95, 24)),
                ],
                spikes=[
                    Spike(pygame.Rect(260, 552, 70, 33), hidden_until_step=1),
                    Spike(pygame.Rect(420, 552, 70, 33), hidden_until_step=2),
                    Spike(pygame.Rect(580, 552, 70, 33), hidden_until_step=3),
                    Spike(pygame.Rect(740, 552, 70, 33), hidden_until_step=4),
                ],
                messages=[
                    MessageZone(pygame.Rect(100, 460, 130, 90), "Шипы появляются, когда подходишь. Оглядывайся.", True),
                ],
                door=pygame.Rect(845, 274, 42, 66),
                fake_door=pygame.Rect(650, 274, 42, 66),
                reveal_points=(220, 280, 340, 400, 460, 520),
            ),
            Level(
                name="Комната 6: Двери повсюду",
                spawn=(55, 505),
                platforms=[
                    Platform(pygame.Rect(0, 585, 960, 55)),
                    Platform(pygame.Rect(100, 510, 140, 24)),
                    Platform(pygame.Rect(330, 460, 120, 24)),
                    Platform(pygame.Rect(540, 400, 120, 24)),
                    Platform(pygame.Rect(730, 340, 120, 24)),
                    Platform(pygame.Rect(810, 490, 95, 24)),
                ],
                spikes=[
                    Spike(pygame.Rect(250, 552, 70, 33)),
                    Spike(pygame.Rect(480, 552, 70, 33)),
                ],
                messages=[
                    MessageZone(pygame.Rect(80, 460, 160, 90), "Только одна дверь настоящая. Остальные... не очень.", True),
                ],
                door=pygame.Rect(840, 274, 42, 66),
                fake_door=pygame.Rect(730, 274, 42, 66),
            ),
            Level(
                name="Комната 7: Падающий потолок",
                spawn=(65, 505),
                platforms=[
                    Platform(pygame.Rect(0, 585, 960, 55)),
                    Platform(pygame.Rect(140, 510, 130, 24)),
                    Platform(pygame.Rect(320, 455, 110, 24)),
                    Platform(pygame.Rect(490, 395, 110, 24)),
                    Platform(pygame.Rect(650, 335, 120, 24)),
                    Platform(pygame.Rect(810, 490, 95, 24)),
                ],
                spikes=[],
                messages=[
                    MessageZone(pygame.Rect(100, 460, 140, 90), "Сверху что-то падает. Не стой на месте.", True),
                    MessageZone(pygame.Rect(600, 290, 120, 80), "Шипы падают с потолка. Беги.", True),
                ],
                door=pygame.Rect(848, 269, 42, 66),
                fake_door=pygame.Rect(740, 445, 42, 66),
                falling=[
                    FallingObstacle(pygame.Rect(265, 552, 70, 33), start_y=72, trigger_x=265, speed=300),
                    FallingObstacle(pygame.Rect(430, 552, 70, 33), start_y=72, trigger_x=430, speed=300),
                    FallingObstacle(pygame.Rect(595, 552, 70, 33), start_y=72, trigger_x=595, speed=300),
                    FallingObstacle(pygame.Rect(760, 552, 70, 33), start_y=72, trigger_x=760, speed=300),
                ],
            ),
            Level(
                name="Комната 8: Вертикальный подъём",
                spawn=(70, 505),
                platforms=[
                    Platform(pygame.Rect(0, 585, 960, 55)),
                    Platform(pygame.Rect(120, 510, 110, 24)),
                    Platform(pygame.Rect(290, 450, 100, 24)),
                    Platform(pygame.Rect(440, 390, 100, 24)),
                    Platform(pygame.Rect(580, 330, 100, 24), hidden_until_step=1),
                    Platform(pygame.Rect(720, 270, 100, 24)),
                    Platform(pygame.Rect(810, 490, 95, 24)),
                ],
                spikes=[
                    Spike(pygame.Rect(235, 552, 70, 33), hidden_until_step=2),
                    Spike(pygame.Rect(380, 552, 70, 33)),
                    Spike(pygame.Rect(530, 552, 70, 33)),
                    Spike(pygame.Rect(670, 552, 70, 33), hidden_until_step=3),
                ],
                messages=[
                    MessageZone(pygame.Rect(50, 440, 120, 90), "Лестница в никуда. Или куда-то.", True),
                ],
                door=pygame.Rect(835, 204, 42, 66),
                fake_door=pygame.Rect(810, 434, 42, 66),
                reveal_points=(260, 360, 460, 560, 660, 760),
            ),
            Level(
                name="Комната 9: Узкая тропа",
                spawn=(60, 505),
                platforms=[
                    Platform(pygame.Rect(0, 585, 960, 55)),
                    Platform(pygame.Rect(100, 505, 80, 24)),
                    Platform(pygame.Rect(240, 455, 80, 24)),
                    Platform(pygame.Rect(380, 395, 80, 24), vanish_on_touch=True),
                    Platform(pygame.Rect(520, 335, 80, 24)),
                    Platform(pygame.Rect(660, 280, 80, 24), vanish_on_touch=True),
                    Platform(pygame.Rect(800, 500, 95, 24)),
                ],
                spikes=[
                    Spike(pygame.Rect(195, 552, 70, 33)),
                    Spike(pygame.Rect(335, 552, 70, 33)),
                    Spike(pygame.Rect(475, 552, 70, 33), hidden_until_step=2),
                    Spike(pygame.Rect(615, 552, 70, 33)),
                    Spike(pygame.Rect(755, 552, 70, 33), hidden_until_step=3),
                ],
                messages=[
                    MessageZone(pygame.Rect(60, 450, 140, 90), "Платформы маленькие и исчезают. Точно.", True),
                ],
                door=pygame.Rect(850, 214, 42, 66),
                fake_door=pygame.Rect(820, 434, 42, 66),
                reveal_points=(200, 300, 400, 500, 600, 700),
            ),
            Level(
                name="Комната 10: Развилка",
                spawn=(65, 505),
                platforms=[
                    Platform(pygame.Rect(0, 585, 960, 55)),
                    Platform(pygame.Rect(140, 510, 140, 24)),
                    Platform(pygame.Rect(350, 460, 110, 24)),
                    Platform(pygame.Rect(520, 400, 100, 24)),
                    Platform(pygame.Rect(660, 340, 100, 24), vanish_on_touch=True),
                    Platform(pygame.Rect(790, 490, 110, 24)),
                    Platform(pygame.Rect(400, 320, 80, 24), hidden_until_step=2),
                ],
                spikes=[
                    Spike(pygame.Rect(290, 552, 80, 33)),
                    Spike(pygame.Rect(470, 552, 80, 33), hidden_until_step=1),
                    Spike(pygame.Rect(610, 552, 80, 33)),
                    Spike(pygame.Rect(730, 552, 80, 33)),
                ],
                messages=[
                    MessageZone(pygame.Rect(90, 460, 140, 90), "Два пути. Оба ведут к боли. Выбирай.", True),
                    MessageZone(pygame.Rect(360, 280, 120, 80), "Верхний путь — секрет. Или ловушка.", True),
                ],
                door=pygame.Rect(852, 424, 42, 66),
                fake_door=pygame.Rect(720, 274, 42, 66),
                reveal_points=(240, 340, 440, 540, 640, 740),
            ),
            Level(
                name="Комната 11: Хаос",
                spawn=(55, 505),
                platforms=[
                    Platform(pygame.Rect(0, 585, 960, 55)),
                    Platform(pygame.Rect(120, 515, 120, 24), vanish_on_touch=True),
                    Platform(pygame.Rect(290, 460, 100, 24)),
                    Platform(pygame.Rect(440, 400, 100, 24), vanish_on_touch=True),
                    Platform(pygame.Rect(570, 340, 100, 24)),
                    Platform(pygame.Rect(700, 280, 100, 24), vanish_on_touch=True),
                    Platform(pygame.Rect(800, 480, 95, 24)),
                ],
                spikes=[
                    Spike(pygame.Rect(230, 552, 70, 33)),
                    Spike(pygame.Rect(390, 552, 70, 33), hidden_until_step=1),
                    Spike(pygame.Rect(520, 552, 70, 33)),
                    Spike(pygame.Rect(650, 552, 70, 33), hidden_until_step=3),
                ],
                messages=[
                    MessageZone(pygame.Rect(60, 460, 140, 90), "Всё сразу: исчезают, падают, появляются. Удачи.", True),
                ],
                door=pygame.Rect(848, 214, 42, 66),
                fake_door=pygame.Rect(720, 444, 42, 66),
                reveal_points=(220, 320, 420, 520, 620, 720),
                falling=[
                    FallingObstacle(pygame.Rect(340, 552, 70, 33), start_y=72, trigger_x=340, speed=350),
                    FallingObstacle(pygame.Rect(550, 552, 70, 33), start_y=72, trigger_x=550, speed=350),
                ],
            ),
            Level(
                name="Комната 12: Финал",
                spawn=(70, 505),
                platforms=[
                    Platform(pygame.Rect(0, 585, 960, 55)),
                    Platform(pygame.Rect(100, 510, 120, 24), vanish_on_touch=True),
                    Platform(pygame.Rect(270, 450, 100, 24)),
                    Platform(pygame.Rect(420, 390, 100, 24), vanish_on_touch=True),
                    Platform(pygame.Rect(560, 330, 100, 24)),
                    Platform(pygame.Rect(690, 270, 100, 24), hidden_until_step=2),
                    Platform(pygame.Rect(570, 500, 200, 24), hidden_until_step=4),
                    Platform(pygame.Rect(810, 480, 95, 24)),
                ],
                spikes=[
                    Spike(pygame.Rect(220, 552, 70, 33), hidden_until_step=1),
                    Spike(pygame.Rect(370, 552, 70, 33)),
                    Spike(pygame.Rect(510, 552, 70, 33), hidden_until_step=3),
                    Spike(pygame.Rect(650, 552, 70, 33)),
                    Spike(pygame.Rect(800, 552, 70, 33), hidden_until_step=5),
                ],
                messages=[
                    MessageZone(pygame.Rect(30, 380, 140, 100), "Финальная комната. Всё, чему ты научился. Или нет.", True),
                    MessageZone(pygame.Rect(520, 460, 130, 80), "Дверь наверху. Как всегда.", True),
                ],
                door=pygame.Rect(855, 204, 42, 66),
                fake_door=pygame.Rect(830, 434, 42, 66),
                reveal_points=(200, 300, 400, 500, 600, 700),
                falling=[
                    FallingObstacle(pygame.Rect(420, 552, 70, 33), start_y=72, trigger_x=420, speed=350),
                    FallingObstacle(pygame.Rect(700, 552, 70, 33), start_y=72, trigger_x=700, speed=350),
                ],
            ),
        ]

    def start_game(self):
        self.playing = True
        self.level_index = 0
        self.level = self.levels[0]
        self.player = Player(self.level.spawn)
        self.deaths = 0
        self.reveal_stage = 0
        self.max_player_x = self.player.rect.centerx
        self.finished = False
        self.toast = self.tr("toast_intro")
        self.toast_timer = 3.0
        self.camera_shake = 0

    def current_offset(self):
        if self.camera_shake <= 0:
            return pygame.Vector2(0, 0)
        amount = int(self.camera_shake)
        return pygame.Vector2((pygame.time.get_ticks() // 40) % (amount * 2 + 1) - amount, 0)

    def set_toast(self, text, seconds=2.3):
        self.toast = text
        self.toast_timer = seconds

    def load_level(self, index):
        self.level_index = index
        self.level = self.levels[self.level_index]
        self.player.reset(self.level.spawn)
        self.reveal_stage = 0
        self.max_player_x = self.player.rect.centerx
        for platform in self.level.platforms:
            platform.touched = False
        for msg in self.level.messages:
            msg.shown = False
        self.falling_obstacles = [
            FallingObstacle(
                rect=f.rect,
                start_y=f.start_y,
                trigger_x=f.trigger_x or f.rect.centerx,
                speed=f.speed,
                current_y=float(f.start_y),
            )
            for f in self.level.falling
        ]
        self.set_toast(self.level.name)

    def die(self, reason):
        self.deaths += 1
        self.camera_shake = 9
        self.set_toast(reason, 1.7)
        self.load_level(self.level_index)

    def next_level(self):
        if self.level_index + 1 >= len(self.levels):
            self.finished = True
            self.set_toast(self.tr("finish_toast"), 8)
            return
        self.load_level(self.level_index + 1)

    def active_platforms(self):
        return [
            p for p in self.level.platforms
            if self.reveal_stage >= p.hidden_until_step and not (p.vanish_on_touch and p.touched)
        ]

    def active_spikes(self):
        return [s for s in self.level.spikes if s.active and self.reveal_stage >= s.hidden_until_step]

    def physical_platforms(self):
        return self.active_platforms()

    def physical_spikes(self):
        return self.active_spikes()

    def hidden_obstacles_near_reveal(self):
        next_stage = self.reveal_stage + 1
        if next_stage > len(self.level.reveal_points):
            return [], []
        distance = self.level.reveal_points[next_stage - 1] - self.max_player_x
        if distance > 30:
            return [], []
        platforms = [
            p for p in self.level.platforms
            if p.hidden_until_step == next_stage and not (p.vanish_on_touch and p.touched)
        ]
        spikes = [s for s in self.level.spikes if s.active and s.hidden_until_step == next_stage]
        return platforms, spikes

    def update_reveals(self):
        self.max_player_x = max(self.max_player_x, self.player.rect.centerx)
        new_stage = 0
        for index, point in enumerate(self.level.reveal_points, start=1):
            if self.max_player_x >= point:
                new_stage = index
        if new_stage > self.reveal_stage:
            self.reveal_stage = new_stage

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN):
                scale_x = 960 / self.window.get_width()
                scale_y = 640 / self.window.get_height()
                event.pos = (int(event.pos[0] * scale_x), int(event.pos[1] * scale_y))

            if not self.playing:
                self.menu.handle_event(event)
                continue

            if event.type == pygame.KEYDOWN:
                if event.key == self.key_bindings["pause"]:
                    self.playing = False
                    self.menu.state = "paused"
                    self.menu.refresh_texts()
                    return
                if event.key == self.key_bindings["reset"]:
                    self.die(self.tr("die_manual"))
                elif event.key == pygame.K_RETURN and self.finished:
                    self.deaths = 0
                    self.finished = False
                    self.load_level(0)
                elif event.key == self.key_bindings["jump"]:
                    self.player.jump_buffer = JUMP_BUFFER_TIME

    def update(self, dt):
        if self.finished or not self.playing:
            return

        keys = pygame.key.get_pressed()
        self.player.jump_buffer = max(0, self.player.jump_buffer - dt)
        if self.player.on_ground:
            self.player.coyote_timer = COYOTE_TIME
        else:
            self.player.coyote_timer = max(0, self.player.coyote_timer - dt)

        if self.player.jump_buffer > 0 and self.player.coyote_timer > 0:
            self.player.vel.y = -JUMP_SPEED
            self.player.on_ground = False
            self.player.coyote_timer = 0
            self.player.jump_buffer = 0

        self.player.vel.x = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[self.key_bindings["left"]]:
            self.player.vel.x = -MOVE_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[self.key_bindings["right"]]:
            self.player.vel.x = MOVE_SPEED

        self.player.vel.y += GRAVITY * dt
        self.player.rect.x += int(self.player.vel.x * dt)
        self.update_reveals()
        self.resolve_collisions(axis="x")
        self.player.rect.y += int(self.player.vel.y * dt)
        self.player.on_ground = False
        self.resolve_collisions(axis="y")

        if self.player.rect.top > HEIGHT + 80:
            self.die(self.tr("die_fall"))
            return

        for spike in self.physical_spikes():
            if self.player.rect.colliderect(spike.rect):
                self.die(self.tr("die_spike"))
                return

        for ob in self.falling_obstacles:
            if ob.landed and ob.is_spike:
                r = pygame.Rect(ob.rect.x, int(ob.current_y), ob.rect.w, ob.rect.h)
                if self.player.rect.colliderect(r):
                    self.die(self.tr("die_spike"))
                    return

        if self.level.fake_door and self.player.rect.colliderect(self.level.fake_door):
            self.die(self.tr("die_fake"))
            return

        for zone in self.level.messages:
            if self.player.rect.colliderect(zone.rect) and not (zone.once and zone.shown):
                zone.shown = True
                self.set_toast(zone.text)

        if self.player.rect.colliderect(self.level.door):
            self.next_level()

        self.player.rect.left = max(self.player.rect.left, 0)
        self.player.rect.right = min(self.player.rect.right, WIDTH)
        self.toast_timer = max(0, self.toast_timer - dt)
        self.camera_shake = max(0, self.camera_shake - 25 * dt)

        if self.hold_jump:
            held = keys[self.key_bindings["jump"]] or keys[pygame.K_UP] or keys[pygame.K_w]
            if held and self.player.on_ground:
                self.player.vel.y = -JUMP_SPEED
                self.player.on_ground = False

        for ob in self.falling_obstacles:
            if not ob.active and self.player.rect.right >= ob.trigger_x:
                ob.active = True
            if ob.active and not ob.landed:
                ob.current_y += ob.speed * dt
                if ob.current_y >= ob.rect.y:
                    ob.current_y = ob.rect.y
                    ob.landed = True

    def resolve_collisions(self, axis):
        for platform in self.physical_platforms():
            if not self.player.rect.colliderect(platform.rect):
                continue

            if platform.vanish_on_touch and axis == "y" and self.player.vel.y >= 0:
                platform.touched = True

            if axis == "x":
                if self.player.vel.x > 0:
                    self.player.rect.right = platform.rect.left
                elif self.player.vel.x < 0:
                    self.player.rect.left = platform.rect.right
            else:
                if self.player.vel.y > 0:
                    self.player.rect.bottom = platform.rect.top
                    self.player.vel.y = 0
                    self.player.on_ground = True
                elif self.player.vel.y < 0:
                    self.player.rect.top = platform.rect.bottom
                    self.player.vel.y = 80

    def draw_platform(self, platform, offset):
        rect = platform.rect.move(offset)
        texture = self.textures["vanish"] if platform.vanish_on_touch else self.textures["brick"]
        for x in range(rect.left, rect.right, texture.get_width()):
            for y in range(rect.top, rect.bottom, texture.get_height()):
                self.screen.blit(texture, (x, y), pygame.Rect(0, 0, rect.right - x, rect.bottom - y))
        pygame.draw.rect(self.screen, STONE_DARK, rect, 2)

    def draw_platform_hint(self, platform, offset, origin):
        rect = pygame.Rect(platform.rect)
        rect.topleft = origin
        color = BLUE if platform.vanish_on_touch else STONE_LIGHT
        hint = pygame.Surface(rect.size, pygame.SRCALPHA)
        pygame.draw.rect(hint, (*color, 55), hint.get_rect())
        pygame.draw.rect(hint, (*WHITE, 115), hint.get_rect(), 2)
        self.screen.blit(hint, rect.topleft)

    def draw_spike(self, spike, offset):
        x, y, w, h = spike.rect.move(offset)
        count = max(1, w // 20)
        for i in range(count):
            left = x + i * (w / count)
            right = x + (i + 1) * (w / count)
            mid = (left + right) / 2
            points = [(left, y + h), (mid, y), (right, y + h)]
            pygame.draw.polygon(self.screen, BONE, points)
            pygame.draw.polygon(self.screen, INK, points, 2)
            pygame.draw.line(self.screen, WHITE, (mid - 3, y + 9), (mid - 8, y + h - 5), 1)

    def draw_spike_hint(self, spike, offset, origin):
        x, y = origin
        w, h = spike.rect.size
        count = max(1, w // 20)
        hint = pygame.Surface((w, h), pygame.SRCALPHA)
        for i in range(count):
            left = i * (w / count)
            right = (i + 1) * (w / count)
            mid = (left + right) / 2
            points = [(left, h), (mid, 0), (right, h)]
            pygame.draw.polygon(hint, (*RED, 45), points)
            pygame.draw.polygon(hint, (*WHITE, 125), points, 1)
        self.screen.blit(hint, (x, y))

    def draw_reveal_hints(self, offset):
        platforms, spikes = self.hidden_obstacles_near_reveal()
        player_rect = self.player.rect.move(offset)
        moving_right = self.player.vel.x > 0
        base_x = player_rect.right + 10 if moving_right else player_rect.left - 10 - 48
        base_y = player_rect.top + 10
        for index, platform in enumerate(platforms):
            self.draw_platform_hint(platform, offset, (base_x, base_y + index * 24))
        for index, spike in enumerate(spikes):
            self.draw_spike_hint(spike, offset, (base_x, base_y + index * 24 + 12))

    def draw_door(self, rect, offset):
        draw_rect = rect.move(offset)
        pole_x = draw_rect.centerx
        pygame.draw.line(self.screen, WHITE, (pole_x, draw_rect.bottom), (pole_x, draw_rect.top), 3)
        flag = pygame.Rect(pole_x + 2, draw_rect.top, 20, 14)
        pygame.draw.rect(self.screen, MINT, flag)
        pygame.draw.rect(self.screen, WHITE, flag, 1)
        base = pygame.Rect(draw_rect.left, draw_rect.bottom - 4, draw_rect.width, 4)
        pygame.draw.rect(self.screen, STONE, base)

    def draw_player(self, offset):
        rect = self.player.rect.move(offset)
        pygame.draw.rect(self.screen, BLACK, rect)
        inner = rect.inflate(-4, -4)
        pygame.draw.rect(self.screen, (45, 50, 70), inner)
        pygame.draw.rect(self.screen, BLACK, rect, 2)

    def draw_hud(self):
        pygame.draw.rect(self.screen, BLACK, pygame.Rect(0, 0, WIDTH, 72))
        pygame.draw.line(self.screen, STONE_LIGHT, (0, 71), (WIDTH, 71), 2)
        title = self.title_font.render(self.tr("title"), True, WHITE)
        subtitle = self.small.render(self.tr("subtitle"), True, STONE_LIGHT)
        self.screen.blit(title, (24, 10))
        self.screen.blit(subtitle, (27, 45))

        deaths = self.font.render(f"{self.tr('deaths')}: {self.deaths}", True, GOLD)
        room = self.font.render(f"{self.tr('room')}: {self.level_index + 1}/{len(self.levels)}", True, GOLD)
        self.screen.blit(deaths, (WIDTH - deaths.get_width() - room.get_width() - 62, 22))
        self.screen.blit(room, (WIDTH - room.get_width() - 28, 22))

    def wrapped_lines(self, text, font, max_width):
        words = text.split()
        lines = []
        current = ""
        for word in words:
            attempt = f"{current} {word}".strip()
            if font.size(attempt)[0] <= max_width:
                current = attempt
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
        return lines

    def draw_toast(self):
        if self.toast_timer <= 0:
            return
        lines = self.wrapped_lines(self.toast, self.small, WIDTH - 120)
        rendered = [self.small.render(line, True, WHITE) for line in lines]
        box_width = max(line.get_width() for line in rendered) + 20
        box_height = len(rendered) * 19 + 12
        box = pygame.Rect(0, 0, box_width, box_height)
        box.midbottom = (WIDTH // 2, HEIGHT - 16)
        panel = pygame.Surface(box.size, pygame.SRCALPHA)
        pygame.draw.rect(panel, (*BLACK, 150), panel.get_rect())
        pygame.draw.rect(panel, (*GOLD, 115), panel.get_rect(), 1)
        self.screen.blit(panel, box.topleft)
        for index, line in enumerate(rendered):
            line.set_alpha(205)
            self.screen.blit(line, (box.x + 10, box.y + 6 + index * 19))

    def draw_background(self, offset=None):
        self.screen.fill(SKY_DARK)
        off_x = int(offset.x) if offset else 0
        wall = self.textures["wall"]
        for x in range(-off_x, WIDTH, wall.get_width()):
            for y in range(72, HEIGHT, wall.get_height()):
                self.screen.blit(wall, (x, y))
        for y in range(104, HEIGHT, 96):
            pygame.draw.line(self.screen, (32, 36, 52), (0, y), (WIDTH, y), 2)

    def draw_finished(self):
        self.draw_background()
        self.draw_hud()
        text = self.big.render(self.tr("finish_title"), True, MINT)
        self.screen.blit(text, text.get_rect(center=(WIDTH // 2, 230)))
        stats = self.font.render(f"{self.tr('finish_stats')}: {self.deaths}", True, WHITE)
        self.screen.blit(stats, stats.get_rect(center=(WIDTH // 2, 300)))
        again = self.font.render(self.tr("finish_again"), True, GOLD)
        self.screen.blit(again, again.get_rect(center=(WIDTH // 2, 365)))
        esc = self.small.render(self.tr("finish_esc"), True, WHITE)
        self.screen.blit(esc, esc.get_rect(center=(WIDTH // 2, 408)))

    def draw_menu_background(self, state):
        self.screen.fill(SKY_DARK)
        wall = self.textures["wall"]
        for x in range(0, WIDTH, wall.get_width()):
            for y in range(0, HEIGHT, wall.get_height()):
                self.screen.blit(wall, (x, y))

        label = self.tr("menu_pause") if state == "paused" else self.tr("title")
        title = self.big.render(label, True, GOLD)
        self.screen.blit(title, title.get_rect(center=(WIDTH // 2, 100)))

        subs = {"settings": self.tr("settings"), "controls": self.tr("controls")}
        if state in subs:
            sub = self.small.render(subs[state], True, STONE_LIGHT)
            self.screen.blit(sub, sub.get_rect(center=(WIDTH // 2, 140)))

    def draw(self):
        if not self.playing:
            self.draw_menu_background(self.menu.state)
            for btn in self.menu.buttons.get(self.menu.state, []):
                btn.draw(self.screen, self.menu_font)
            self.draw_toast()
            return

        if self.finished:
            self.draw_finished()
            self.draw_toast()
            return

        offset = self.current_offset()
        self.draw_background(offset)
        for platform in self.active_platforms():
            self.draw_platform(platform, offset)
        for spike in self.active_spikes():
            self.draw_spike(spike, offset)
        for ob in self.falling_obstacles:
            if ob.active:
                s = Spike(pygame.Rect(ob.rect.x, int(ob.current_y), ob.rect.w, ob.rect.h))
                self.draw_spike(s, offset)
        self.draw_door(self.level.door, offset)
        if self.level.fake_door:
            self.draw_door(self.level.fake_door, offset)
        self.draw_player(offset)
        self.draw_hud()
        self.draw_toast()

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000
            self.handle_events()
            self.update(dt)
            self.screen = self.internal
            self.draw()
            win_w, win_h = self.window.get_size()
            aspect = WIDTH / HEIGHT
            win_aspect = win_w / win_h
            if win_aspect > aspect:
                scaled_h = win_h
                scaled_w = int(scaled_h * aspect)
            else:
                scaled_w = win_w
                scaled_h = int(scaled_w / aspect)
            scaled = pygame.transform.scale(self.internal, (scaled_w, scaled_h))
            self.window.fill(BLACK)
            self.window.blit(scaled, ((win_w - scaled_w) // 2, (win_h - scaled_h) // 2))
            pygame.display.flip()
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    Game().run()