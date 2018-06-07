import math
def receptive_field(n, layers, position):
    """
    Parameters
    ----------
    n: int, input size
    layers: array of triplets: (k,s,p)
        k: kernel size
        s: stride
        p: padding
    
    Returns
    -------
    n: output size
    j: jump size
    r: size of receptive field
    start: center position of the receptive field of the first output feature
    """

    r = 1
    j = 1
    start = 0.5
    for k, s, p in layers:
        n = math.floor( (n - k + p)/s ) + 1
        r = r + (k-1)*j
        start = start + ( (k-1)/2 - p)*j
        j = j*s
        print(int(n), j, r, start)

    #return int(n), j, r, start
    x1 = (position[0]+1)*start
    y1 = (position[1]+1)*start

    x2 = (position[2]+1)*start
    y2 = (position[3]+1)*start
    print('Position : ',int(x1-r//2), int(y1-r//2), int(x2+r//2)-1, int(y2+r//2)-1)


# Example:
layers = [
    (3, 2, 0), # k, s, p
    (3, 2, 0),
    # (1, 4, 0), # maxpool
    # (16, 8, 8),
    # (16, 8, 8),
]
receptive_field(32, layers, [0,0,2,2])
#> (0, 4096, 8796, -640.5)