from PIL import Image


def convert(image, font):
    img = Image.open(image)
    values = []
    for line in range(img.height//8):
        for x in range(img.width):
            if (x+1)%6 == 0:
                continue
            line_y = line * 9
            line_val = 0
            for iy in range(8):
                y = line_y + iy
                px = img.getpixel((x, y))
                if sum(px) < 765:  # NOT white
                    line_val += 1 << iy
            values.append(line_val)

    with open(font, "w") as f:
        print("#ifndef FONT_H_", file=f)
        print("#define FONT_H_", file=f)
        print("#include <stdint.h>", file=f)
        print("const uint8_t font[] = {", file=f)
        for v in values[:-25]:
            print(f"  0b{v:08b},", file=f)
        print("};", file=f)
        print("#endif  // FONT_H_", file=f)


def main() -> None:
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("image")
    parser.add_argument("font")
    args = parser.parse_args()

    convert(args.image, args.font)


if __name__ == '__main__':
    main()
