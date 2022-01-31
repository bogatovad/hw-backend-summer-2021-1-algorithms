__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    if not seconds:
        return '00s'

    count_sec_in_day = seconds//86400
    count_sec_in_hour = (seconds - count_sec_in_day*86400)//3600
    count_sec_in_min = (seconds - count_sec_in_day*86400 - count_sec_in_hour*3600)//60
    count_s = seconds - count_sec_in_day*86400 - count_sec_in_hour*3600 - count_sec_in_min*60
    time_mark = ((count_sec_in_day,'d'), (count_sec_in_hour, 'h'), (count_sec_in_min, 'm'), (count_s, 's'))
    begin = False
    strtime = ''
    
    for item in time_mark:
        if item[0]:
            begin = True
        
        if begin:
            t = ''
            if item[0] < 10:
                t = f'0{item[0]}{item[1]}'
            else:
                t = f'{item[0]}{item[1]}'
            strtime += t


    return strtime


