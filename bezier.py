from PIL import Image, ImageDraw

def bezier_points(x_and_y, ts):
    # x_and_y are Bezier control points
    n=len(x_and_y)
    combinations=pascal_row(n-1)
    # basic genereal formula for Bezier curves(from Wiki)
    result=[]
    for t in ts:
        # so in formula we have t^i and (1-t)^(n-i)
        left_coefs=(t**i for i in range(n))
        right_coefs=reversed([(1-t)**i for i in range(n)])
        # preparing coefficients of a formula
        coefs=[c*a*b for c,a,b in zip(combinations,left_coefs,right_coefs)]
        # calculating poits for drawing
        # zip(*x_and_y) creates 2 turples with xs and ys
        result.append(
            tuple(
                sum([coef*p for coef,p in zip(coefs,ps)]) for ps in zip(*x_and_y)
            )
        )
   
    return result

def pascal_row(n):
    # returns the nth row of Pascal's Triangle (binomial coefs)
    result=[1]
    x,numerator=1,n
    for denominator in range(1,n//2+1):
        x*=numerator
        x/=denominator
        result.append(x)
        numerator-=1
    # so also we know that they are mirrored
    if n&1==0:
        result.extend(reversed(result[:-1]))
    else:
        result.extend(reversed(result)) 
    return result

im = Image.new('RGBA', (200, 100), (141, 182,199, 100), ) 
draw = ImageDraw.Draw(im)
# draw points
ts=[t/100.0 for t in range(101)]

# points for letter p
xys=[(40,60),(100,20),(30,30),(40,20)]
points_p=bezier_points(xys,ts)

xys=[(40,60),(40,65),(40,100)]
points_p.extend(bezier_points(xys,ts))

#points for letter u(thea are 2 curves)
xys=[(110,20),(150,100),(170,20)]
points_u_1 = (bezier_points(xys,ts))

xys=[(148,58),(145,60),(138,58)]
points_u_1.extend(bezier_points(xys,ts))

xys = [(157,45),(157,50),(110,100)]
points_u_2 = (bezier_points(xys,ts))

draw.polygon(points_p,fill=None,outline='red')

draw.polygon(points_u_1,fill='red',outline='red')

draw.polygon(points_u_2,fill=None,outline='red')

# if you want to save a picture
#im.save('PY.png')
im.show()