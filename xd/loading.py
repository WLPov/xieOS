import tqdm
import time
def loading(text, color):
    for i in tqdm.tqdm(range(1, 101),colour=color,desc=text):
        time.sleep(0.01)
