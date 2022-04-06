from django.http import JsonResponse
from algo_com_clock.get_text_info.atcoder.get_atcoder import AtCoderSpider
from algo_com_clock.get_text_info.codeforces.get_cf import CF_Spider
from algo_com_clock.get_text_info.nowcoder.get_nowcoder import CowSpider

def index(request):
    platform = request.GET.get('platform')

    if platform == 'atcoder':
        return get_atcoder()
    elif platform == 'nowcoder':
        return get_now()



def get_atcoder():
    atc = AtCoderSpider()
    res_json = atc.main()
    # print(res_json)
    return JsonResponse({
        'result' : 'success',
        'info' : res_json
        })


def get_now():
    now = CowSpider()
    res_json = now.main()
    return JsonResponse({
        'result' : 'success',
        'info' : res_json
        })

