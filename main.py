import time

def countdown_timer(seconds):
    while seconds > 0:
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        
        timer_display = f'{minutes:02d}:{remaining_seconds:02d}'
        print(f'\rTime remaining: {timer_display}', end='')
        
        time.sleep(1)
        seconds -= 1
    
    print('\nTime is up!')

if __name__ == '__main__':
    try:
        duration = int(input('Enter countdown duration in seconds: '))
        countdown_timer(duration)
    except ValueError:
        print('Please enter a valid number of seconds')
    except KeyboardInterrupt:
        print('\nTimer cancelled by user')
