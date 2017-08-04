from PIL import Image, ImageFont, ImageDraw
import numpy as np
import color_calc as cc

if __name__ == '__main__':
    #画像サイズ, パターン数を規定（割り切れるように！）
    img_size = (1920,1080)
    gen_code = np.array([(216,202,168), (92,131,47), (40,73,7), (56,37,19), (54,57,66)])

    pat_code = cc.interpolate(gen_code, 4)
    print(pat_code)
    pat_num = int(pat_code[:,1].size)
    pat_size = (int(img_size[0]/pat_num), int(img_size[1]))

    #マージに利用する下地を作成(FULLHDサイズ)
    canvas = Image.new('RGB', img_size, (255,255,255))
    #draw = ImageDraw.Draw(canvas)

    #パターンの各要素を作成
    patt = np.zeros(pat_num)
    print(pat_size)
    for x in range(0,int(pat_num)):
        print(pat_code[x])
        cctup = (pat_code[x,0], pat_code[x,1], pat_code[x,2])
        #print(cctup)
        patt_tmp = Image.new('RGB', pat_size, cctup)
        pos = int(x * pat_size[0])
        print(pos)
        canvas.paste(patt_tmp, (pos, 0))

    #下地にパターンの要素を貼り付け
    #canvas.paste(pat_red,(0,0))
    #canvas.paste(pat_green,(500,0))
    #for x in range[pat_num]:
    #    pos = int(x*img_size[1]/pat_num)
    #    canvas.paste(patt[x], (pos,0))

    #font = ImageFont.truetype('C:\Windows\Fonts\ipaexg.ttf', 80)

    # 指定の座標にテキスト書き込み 書き込み座標, テキスト, フォント, 文字色
    # fill には16進のカラーコード
    #draw.text((960,500), 'Firenze', font=font, fill='#FFFFFF')

    #パターン画像生成
    canvas.save('japanese_garden.jpg', 'JPEG', quality = 100, optimize = True)
