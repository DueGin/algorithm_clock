from json import JSONDecodeError
from django.http import JsonResponse
from algo_com_clock.get_text_info.atcoder.get_atcoder import AtCoderSpider
from algo_com_clock.get_text_info.codeforces.get_cf import CF_Spider
from algo_com_clock.get_text_info.nowcoder.get_nowcoder import CowSpider

def index(request):
    platform = request.GET.get('platform')

    if platform == 'AtCoder':
        return get_atcoder()
    elif platform == 'NowCoder':
        return get_now()
    elif platform == 'CodeForces':
        return get_cf()



def get_atcoder():
    atc = AtCoderSpider()
    res_data = atc.main()
    # print(res_json)
    return JsonResponse({
        'result' : 'success',
        'info' : res_data
        })


def get_now():
    now = CowSpider()
    res_data = now.main()
    return JsonResponse({
        'result' : 'success',
        'info' : res_data
        })


def get_cf():
    cf = CF_Spider()
    res_data = cf.main()
    return JsonResponse({
        'result' : 'success',
        'info' : res_data
    })
