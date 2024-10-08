from math import sqrt

def get_distance(p1, p2):
        x1,y1 = p1
        x2,y2 = p2
        return ((x2 - x1)**2) + ((y2 - y1)**2)

def get_left_nearest(dots, diameter, left):
        nearest = None
        for dot in dots:
            x,y = dot[0]
            dist = int(x - left)
            if dist <= diameter:
                if nearest is None:
                    nearest = dot
                else:
                    X,Y = nearest[0]
                    DIST = int(X - left)
                    if DIST > dist:
                        nearest = dot
        return nearest

def get_right_nearest(dots, diameter, right):
        nearest = None
        for dot in dots:
            x,y = dot[0]
            dist = int(right - x)
            if dist <= diameter:
                if nearest is None:
                    nearest = dot
                else:
                    X,Y = nearest[0]
                    DIST = int(right - X)
                    if DIST > dist:
                        nearest = dot
        return nearest

def get_dot_nearest(dots, diameter, pt1):
        nearest = None
        diameter **= 2
        for dot in dots:
            point = dot[0]
            dist_from_pt1 = get_distance(point, pt1)
            if dist_from_pt1 <= diameter:
                if nearest is None:
                    nearest = dot
                else:
                    pt = nearest[0]
                    ndist_from_pt1 = get_distance(pt, pt1)
                    if ndist_from_pt1 >= dist_from_pt1:
                        nearest = dot
        return nearest



def get_combination(box, dots, diameter):
        result = [0,0,0,0,0,0]
        left,right,top,bottom = box

        midpointY = int((bottom - top)/2)
        end = (right, midpointY)
        start = (left, midpointY)
        width = int(right - left)

        corners = { (left,top): 1, (right,top): 4, (left, bottom): 3, (right,bottom): 6,
                (left): 2, (right): 5}

        for corner in corners:
            if corner != left and corner != right:
                D = get_dot_nearest(dots, int(diameter), corner)
            else:
                if corner == left:
                    D = get_left_nearest(dots, int(diameter), left)
                else:
                    D = get_right_nearest(dots, int(diameter), right)

            if D is not None:
                dots.remove(D)
                result[corners[corner]-1] = 1

            if len(dots) == 0:
                break
        return end,start,width,tuple(result);

def translate_to_number(value):
    if value == 'a':
        return '1'
    elif value == 'b':
        return '2'
    elif value == 'c':
        return '3'
    elif value == 'd':
        return '4'
    elif value == 'e':
        return '5'
    elif value == 'f':
        return '6'
    elif value == 'g':
        return '7'
    elif value == 'h':
        return '8'
    elif value == 'i':
        return '9'
    else:
        return '0'

class Symbol(object):
    def __init__(self, value = None, letter = False, special = False):
        self.is_letter = letter
        self.is_special = special
        self.value = value

    def is_valid(self):
        r = True
        r = r and (self.value is not None)
        r = r and (self.is_letter is not None or self.is_special is not None)
        return r

    def letter(self):
        return self.is_letter

    def special(self):
        return self.is_special

class BrailleClassifier(object):
    symbol_table = {
         (1,1,0,1,1,0): Symbol('ก',letter=True),
         (1,0,1,0,0,0): Symbol('ข',letter=True),
        #  (,,,,,): Symbol('ฃ',letter=True),
         (1,0,1,0,0,1): Symbol('ค',letter=True),
        #  (,,,,,): Symbol('ฅ',letter=True),
        #  (,,,,,): Symbol('ฆ',letter=True),
         (1,1,0,1,1,1): Symbol('ง',letter=True),
         (0,1,0,1,1,0): Symbol('จ',letter=True),
         (0,0,1,1,0,0): Symbol('ฉ',letter=True),
         (0,0,1,1,0,1): Symbol('ช',letter=True),
         (0,1,1,1,0,1): Symbol('ซ',letter=True),
        #  (,,,,,): Symbol('ฌ',letter=True),
        #  (,,,,,): Symbol('ญ',letter=True),
        #  (,,,,,): Symbol('ฎ',letter=True),
        #  (,,,,,): Symbol('ฏ',letter=True),
        #  (,,,,,): Symbol('ฐ',letter=True),
        #  (,,,,,): Symbol('ฑ',letter=True),
        #  (,,,,,): Symbol('ฒ',letter=True),
        #  (,,,,,): Symbol('ณ',letter=True),
         (1,0,0,1,1,0): Symbol('ด',letter=True),
         (1,1,0,0,1,1): Symbol('ต',letter=True),
         (0,1,1,1,1,0): Symbol('ถ',letter=True),
         (0,1,1,1,1,1): Symbol('ท',letter=True),
        #  (,,,,,): Symbol('ธ',letter=True),
         (1,0,1,1,1,0): Symbol('น',letter=True),
         (1,1,1,0,0,1): Symbol('บ',letter=True),
         (1,1,1,1,0,1): Symbol('ป',letter=True),
         (1,1,1,1,0,0): Symbol('ผ',letter=True),
         (1,0,1,1,0,1): Symbol('ฝ',letter=True),
         (1,0,0,1,1,1): Symbol('พ',letter=True),
         (1,1,0,1,0,1): Symbol('ฟ',letter=True),
        #  (,,,,,): Symbol('ภ',letter=True),
         (1,0,1,1,0,0): Symbol('ม',letter=True),
         (1,0,1,1,1,1): Symbol('ย',letter=True),
         (1,1,1,0,1,0): Symbol('ร',letter=True),
         (1,1,1,0,0,0): Symbol('ล',letter=True),
         (0,1,0,1,1,1): Symbol('ว',letter=True),
        #  (,,,,,): Symbol('ศ',letter=True),
        #  (,,,,,): Symbol('ษ',letter=True),
         (0,1,1,1,0,0): Symbol('ส',letter=True),
         (1,1,0,0,1,0): Symbol('ห',letter=True),
        #  (,,,,,): Symbol('ฬ',letter=True),
         (1,0,1,0,1,0): Symbol('อ',letter=True),
         (1,1,1,1,1,1): Symbol('ฮ',letter=True),

         (1,0,0,0,0,0): Symbol('ะ',letter=True),
         (1,0,0,0,0,1): Symbol('า',letter=True),
         (1,1,0,0,0,0): Symbol('ิ',letter=True),
         (0,1,1,0,0,0): Symbol('ี',letter=True),
        (0,1,0,1,0,1): Symbol('ึ',letter=True),
         (0,1,0,0,0,1): Symbol('ื',letter=True),
         (1,0,0,1,0,0): Symbol('ุ',letter=True),
         (0,1,0,0,1,0): Symbol('ู',letter=True),
        #  (,,,,,): Symbol('เะ',special=True),
         (1,1,0,1,0,0): Symbol('เ',letter=True),
        #  (,,,,,): Symbol('แะ',special=True),
         (1,1,0,0,0,1): Symbol('แ',letter=True),
        #  (,,,,,): Symbol('โะ',special=True),
         (0,1,0,1,0,0): Symbol('โ',letter=True),
        #  (,,,,,): Symbol('เาะ',special=True),
        #  (,,,,,): Symbol('อ',special=True),
        #  (,,,,,): Symbol('เอะ',special=True),
        #  (,,,,,): Symbol('เอ',special=True),
        #  (,,,,,): Symbol('เียะ',special=True),
         (1,1,1,0,1,1): Symbol('เีย',letter=True),
        #  (,,,,,): Symbol('เือะ',special=True),
         (1,1,1,1,1,0): Symbol('เือ',letter=True),
        #  (,,,,,): Symbol('ัวะ',special=True),
         (1,0,0,0,1,0): Symbol('ัว',letter=True),
         (1,0,1,0,1,1): Symbol('ำ',letter=True),
         (1,0,0,0,1,1): Symbol('ไ',letter=True),
        #  (,,,,,): Symbol('ใ',special=True),
         (0,1,1,0,1,0): Symbol('เา',letter=True),
        #  (,,,,,): Symbol('ฤ',special=True),
        #  (,,,,,): Symbol('ฤา',special=True),
        #  (,,,,,): Symbol('ฦ',special=True),
        #  (,,,,,): Symbol('ฦา',special=True),

         (0,0,1,0,1,0): Symbol('่',letter=True),
         (0,1,0,0,1,1): Symbol('้',letter=True),
         (0,1,1,0,1,1): Symbol('๊',letter=True),
         (0,1,1,0,0,1): Symbol('๋',letter=True),
         (0,0,1,1,1,0): Symbol('ั',letter=True),
         (0,0,1,0,1,1): Symbol('์',letter=True),
         (0,1,0,0,0,0): Symbol('ๆ',letter=True),
         (0,0,1,0,0,0): Symbol('็',letter=True),
    }

    def __init__(self):
        self.result = ''
        self.shift_on = False
        self.prev_end = None
        self.number = False
        return;

    def push(self, character):
        if not character.is_valid():
            return;
        box = character.get_bounding_box()
        dots = character.get_dot_coordinates()
        diameter = character.get_dot_diameter()
        end,start,width,combination = get_combination(box, dots, diameter)

        if combination not in self.symbol_table:
            self.result += "*"
            return;

        if self.prev_end is not None:
            dist = get_distance(self.prev_end, start)
            if dist*0.5 > (width**2):
                self.result += " "
        self.prev_end = end

        symbol = self.symbol_table[combination]
        if symbol.letter() and self.number:
            self.number = False
            self.result += translate_to_number(symbol.value)
        elif symbol.letter():
            if self.shift_on:
                self.result += symbol.value.upper()
            else:
                self.result += symbol.value
        else:
            if symbol.value == '#':
                self.number = True
        return;

    def digest(self):
        return self.result

    def clear(self):
        self.result = ''
        self.shift_on = False
        self.prev_end = None
        self.number = False
        return;