#bubble sort
from datetime import datetime

def bubbleSort(lst):
    l = lst.copy()
    swapped = False
    count = 0
    for x in range(len(l)):
        for i in range(0, len(l) - x - 1):
            if l[i] > l[i+1]:
                count+=1
                l[i], l[i+1] = l[i+1], l[i]
                swapped = True
                # print(l)
        if not swapped:
            break
    print("Total Comparisons: ", count)
    return l

def selectionSort(lst):
    l = lst.copy();
    count1 = 0
    for i in range(len(l)):
        min_index = i
        for j in range(i+1, len(l)):
            if(l[j] < l[min_index]):
                count1 += 1
                min_index = j
        if min_index != i:
            l[i], l[min_index] = l[min_index], l[i]
            # print(l)



    # print()
    print("Total comparisons: ", count1)
    return l;

def insertionSort(lst):
    l = lst[:]
    n = len(l)

    count = 0

    for i in range(1, n):
        key = l[i]
        j = i - 1
        while j >= 0:
            count += 1
            if l[j] > key:
                l[j + 1] = l[j]
                j -= 1
            else:
                break
        l[j + 1] = key
    
    print("No of comparision: ", count)
    return l


def shellSort(lst):
    l = lst[:]
    n = len(l)
    gap = n // 2
    count = 0;

    while gap > 0:
        for i in range(gap, n):
            temp = l[i]
            j = i
            while j >= gap and l[j - gap] > temp:
                count += 1;
                l[j] = l[j - gap]
                j -= gap
            l[j] = temp  # Place temp in the correct position
        gap //= 2  

    print("no of comparision is: ", count)
    return l  



# l = eval(input("Enter your unsorted list: "))
# l2 = l.copy();
#l = [917, 214, 738, 233, 589, 401, 103, 547, 661, 619, 360, 206, 834, 908, 635, 506, 371, 649, 469, 484, 443, 651, 822, 271, 850, 24, 828, 662, 670, 683, 812, 207, 297, 231, 770, 938, 369, 966, 718, 981, 568, 687, 973, 510, 424, 774, 622, 115, 540, 993, 509, 881, 339, 927, 735, 897, 266, 466, 82, 933, 390, 971, 626, 221, 363, 269, 726, 957, 262, 74, 2, 756, 325, 435, 598, 902, 818, 294, 365, 140, 49, 31, 530, 584, 219, 4, 411, 570, 13, 998, 905, 239, 688, 463, 281, 836, 44, 583, 708, 970, 406, 797, 996, 23, 487, 964, 45, 512, 22, 862, 438, 91, 146, 187, 210, 755, 975, 831, 533, 107, 982, 118, 582, 89, 15, 361, 945, 855, 199, 792, 101, 426, 285, 310, 514, 858, 182, 313, 921, 238, 226, 170, 581, 744, 603, 639, 968, 315, 117, 593, 197, 445, 602, 715, 55, 265, 652, 125, 151, 611, 884, 30, 179, 98, 467, 472, 58, 647, 866, 105, 986, 833, 85, 208, 629, 546, 621, 444, 536, 557, 665, 1, 60, 213, 631, 54, 615, 967, 248, 765, 283, 104, 493, 224, 439, 994, 166, 978, 776, 572, 668, 922, 777, 571, 943, 989, 977, 293, 8, 72, 183, 885, 347, 280, 694, 734, 332, 591, 459, 240, 99, 123, 676, 813, 12, 799, 711, 351, 579, 947, 108, 779, 147, 400, 794, 336, 256, 135, 178, 612, 979, 373, 918, 811, 771, 781, 882, 56, 830, 40, 261, 216, 243, 222, 729, 666, 408, 780, 301, 321, 403, 18, 225, 106, 594, 544, 323, 446, 124, 697, 709, 21, 379, 690, 80, 177, 414, 769, 436, 131, 859, 873, 498, 956, 550, 677, 939, 861, 942, 399, 505, 634, 128, 139, 195, 395, 904, 228, 53, 37, 217, 901, 731, 875, 76, 840, 314, 270, 983, 295, 698, 355, 961, 772, 521, 433, 185, 894, 561, 768, 722, 503, 302, 801, 307, 462, 331, 558, 429, 430, 354, 496, 267, 930, 507, 3, 494, 235, 160, 537, 153, 277, 90, 760, 846, 551, 803, 628, 520, 674, 784, 578, 754, 19, 171, 485, 701, 695, 658, 499, 450, 366, 229, 223, 63, 457, 352, 163, 555, 883, 258, 357, 853, 644, 835, 456, 949, 387, 597, 486, 613, 534, 201, 26, 633, 172, 142, 353, 292, 525, 733, 743, 518, 965, 180, 62, 165, 144, 963, 655, 974, 364, 636, 637, 27, 531, 829, 386, 849, 34, 495, 71, 36, 654, 848, 92, 97, 789, 607, 1000, 556, 490, 871, 608, 9, 396, 681, 887, 168, 552, 816, 527, 304, 549, 827, 773, 122, 791, 802, 599, 959, 667, 116, 232, 625, 684, 383, 6, 810, 865, 588, 279, 250, 923, 950, 972, 700, 113, 736, 888, 252, 960, 705, 260, 819, 254, 489, 725, 67, 874, 470, 984, 402, 916, 66, 156, 535, 11, 303, 264, 953, 740, 381, 640, 895, 50, 479, 192, 931, 504, 823, 627, 838, 203, 215, 632, 344, 997, 367, 606, 643, 798, 903, 454, 358, 127, 713, 356, 569, 806, 941, 48, 388, 481, 962, 824, 847, 150, 425, 419, 319, 253, 538, 410, 524, 93, 478, 328, 329, 17, 193, 418, 461, 25, 79, 609, 575, 815, 420, 920, 720, 335, 976, 389, 511, 587, 878, 154, 95, 374, 230, 428, 929, 508, 946, 368, 68, 421, 787, 377, 263, 860, 126, 157, 590, 75, 856, 241, 346, 648, 94, 220, 529, 189, 324, 473, 317, 244, 501, 790, 617, 714, 326, 663, 38, 276, 370, 334, 516, 863, 442, 51, 935, 57, 102, 528, 384, 891, 455, 42, 282, 497, 805, 650, 703, 560, 630, 502, 752, 793, 526, 892, 458, 69, 909, 660, 392, 653, 311, 664, 541, 337, 954, 564, 889, 618, 710, 468, 449, 452, 330, 596, 257, 404, 375, 795, 47, 825, 832, 624, 284, 915, 164, 586, 87, 641, 275, 100, 932, 391, 312, 782, 46, 251, 453, 913, 573, 605, 59, 592, 786, 184, 121, 992, 14, 845, 188, 475, 574, 451, 969, 434, 393, 237, 689, 305, 808, 566, 656, 191, 800, 29, 746, 748, 616, 747, 61, 880, 202, 88, 753, 796, 110, 896, 274, 372, 601, 141, 778, 867, 686, 405, 763, 857, 696, 200, 289, 308, 716, 492, 488, 138, 646, 167, 727, 553, 766, 739, 65, 288, 513, 133, 149, 899, 259, 176, 868, 474, 174, 255, 413, 645, 246, 712, 338, 893, 78, 52, 980, 914, 77, 161, 83, 719, 345, 898, 685, 955, 296, 16, 447, 382, 577, 306, 86, 427, 693, 730, 136, 732, 300, 378, 7, 906, 173, 699, 41, 750, 638, 155, 169, 565, 539, 491, 500, 112, 482, 604, 925, 990, 32, 204, 96, 407, 545, 194, 877, 879, 675, 119, 385, 988, 934, 682, 422, 35, 483, 936, 991, 907, 242, 340, 181, 912, 236, 886, 376, 464, 820, 286, 870, 322, 839, 448, 600, 320, 707, 567, 706, 196, 416, 762, 702, 900, 911, 348, 158, 723, 152, 175, 137, 623, 543, 610, 764, 64, 441, 562, 209, 673, 81, 924, 999, 134, 318, 890, 114, 343, 460, 841, 757, 532, 749, 28, 783, 272, 952, 43, 659, 523, 350, 245, 471, 948, 515, 958, 198, 268, 476, 680, 669, 522, 162, 362, 380, 842, 249, 437, 737, 717, 987, 517, 342, 327, 580, 341, 227, 554, 417, 704, 807, 944, 837, 143, 120, 728, 234, 585, 761, 431, 10, 679, 826, 620, 148, 758, 432, 109, 724, 287, 741, 576, 563, 298, 672, 415, 809, 864, 218, 843, 33, 316, 398, 928, 299, 788, 785, 751, 542, 759, 290, 559, 852, 130, 548, 477, 186, 309, 211, 359, 657, 465, 412, 39, 333, 423, 745, 767, 278, 20, 84, 876, 872, 817, 205, 642, 291, 678, 212, 692, 145, 919, 159, 349, 854, 5, 129, 691, 671, 397, 814, 940, 394, 273, 742, 985, 951, 73, 821, 804, 937, 132, 595, 775, 111, 910, 614, 519, 440, 851, 926, 844, 409, 70, 190, 721, 480, 869, 247, 995]

n = 100000  # Specify the size of the list
min_value = 0
max_value = 100000
l = [random.randint(min_value, max_value) for _ in range(n)]
print("Sorted list:")
starttime1 = datetime.now()

print("Sorted list:")
starttime1 = datetime.now()

print()
print("BUBBLE SORT")
print(bubbleSort(l))
endtime1 = datetime.now()
print("\nTime taken:")
print((endtime1.timestamp() * 1000 - starttime1.timestamp() * 1000), " ms")

print()
print("SELECTION SORT")
starttime2 = datetime.now()
print(selectionSort(l))
endtime2 = datetime.now()
print("\nTime taken:")
print((endtime2.timestamp() * 1000 - starttime2.timestamp() * 1000), " ms")

print()
print("INSERTION SORT")
starttime3 = datetime.now()
print(selectionSort(l))
endtime3 = datetime.now()
print("\nTime taken:")
print((endtime3.timestamp() * 1000 - starttime3.timestamp() * 1000), " ms")

print()
print("SHELL SORT")
starttime4 = datetime.now()
print(shellSort(l))
endtime4 = datetime.now()
print("\nTime taken:")
print((endtime4.timestamp() * 1000 - starttime4.timestamp() * 1000), " ms")
