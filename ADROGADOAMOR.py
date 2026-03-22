import time
import sys
import os
import threading

# --- 1. CONFIGURAÇÕES ---
TOTAL_MUSIC_DURATION = 105.0 
RESET = "\033[0m"
BOLD = "\033[1m"
INACTIVE_LYRIC_COLOR = "\033[38;5;239m" 
INFO_COLOR = "\033[1;36m" 
ROSA = "\033[38;5;211m"

HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"

screen_lock = threading.Lock()

CONTENT_INFO = {
    "title_lines": ["A Droga do Amor (Acústico)"],
    "artist_lines": ["Ari, Felipe Play, Dom R, Tiankris"]
}

# --- 2. DADOS COM TEMPOS ANTECIPADOS (MAIS RÁPIDO) ---
LYRICS_DATA = [
    {"time": 0.0,   "original": "--- introdução ---", "is_refrao": False},
    {"time": 13.5,  "original": "hoje eu vou te levar pro melhor lugar", "is_refrao": False},
    {"time": 17.2,  "original": "perto das estrelas, de frente pro mar", "is_refrao": False},
    {"time": 20.8,  "original": "eu tenho pouco a dizer", "is_refrao": False},
    {"time": 24.2,  "original": "eu prefiro fazer...", "is_refrao": False},
    {"time": 28.0,  "original": "hoje eu vou te levar pro melhor lugar", "is_refrao": False},
    {"time": 31.5,  "original": "perto das estrelas, de frente pro mar", "is_refrao": False},
    {"time": 35.2,  "original": "eu tenho pouco a dizer", "is_refrao": False},
    {"time": 39.0,  "original": "eu prefiro fazer.", "is_refrao": False},
    
    # REFRÃO (Ajustado para entrar no "taco")
    {"time": 43.0,  "original": "seu beijo pode me drogar", "is_refrao": True},
    {"time": 46.5,  "original": "eu odeio me apaixonar", "is_refrao": True},
    {"time": 50.2,  "original": "tudo que ela quer me dar", "is_refrao": True},
    {"time": 54.0,  "original": "o amor pode me drogar", "is_refrao": True},
    {"time": 57.5,  "original": "eu odeio me apaixonar", "is_refrao": True},
    {"time": 61.2,  "original": "será que ela vai voltar?", "is_refrao": True},
    {"time": 65.0,  "original": "seu beijo pode me drogar", "is_refrao": True},
    {"time": 68.8,  "original": "o amor pode me drogar", "is_refrao": True},
    
    {"time": 72.5,  "original": "me drogar, te amar, me drogar, te amar...", "is_refrao": False},
    {"time": 80.0,  "original": "te amar, me drogar, te amar, me drogar...", "is_refrao": False},
    {"time": 87.5,  "original": "a droga do amor... a droga do amor", "is_refrao": False},
    {"time": 94.8,  "original": "a droga do amor... a droga do amor", "is_refrao": False},
]

def display_content(current_line_index, lyrics_data, content_info):
    with screen_lock:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Cabeçalho fixo no topo
        print(f"{BOLD}{INFO_COLOR}{content_info['title_lines'][0]}{RESET}")
        print(f"{INFO_COLOR}{content_info['artist_lines'][0]}{RESET}")
        print("\n" * 3) # Espaço para centralizar a letra
        
        # Mostra a linha anterior (apagada), a ATUAL (brilhante) e as próximas
        start_view = max(0, current_line_index - 1)
        for i in range(start_view, min(start_view + 5, len(lyrics_data))):
            is_active = (i == current_line_index)
            line_data = lyrics_data[i]
            
            if is_active:
                color = (BOLD + ROSA) if line_data["is_refrao"] else BOLD
                prefix = "  >>> "
            else:
                color = INACTIVE_LYRIC_COLOR
                prefix = "      "
            
            print(f"{color}{prefix}{line_data['original']}{RESET}")

def start_lyrics_animation():
    sys.stdout.write(HIDE_CURSOR)
    start_time = time.monotonic()
    ultimo_indice = -1
    
    try:
        while True:
            elapsed = time.monotonic() - start_time
            if elapsed > TOTAL_MUSIC_DURATION: break

            current_idx = 0
            for i, line in enumerate(LYRICS_DATA):
                if elapsed >= line["time"]:
                    current_idx = i
            
            if current_idx != ultimo_indice:
                display_content(current_idx, LYRICS_DATA, CONTENT_INFO)
                ultimo_indice = current_idx
                
            time.sleep(0.01) # Diminuído para 0.01 para resposta instantânea
            
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write(SHOW_CURSOR)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Música finalizada.")

if __name__ == "__main__":
    start_lyrics_animation()