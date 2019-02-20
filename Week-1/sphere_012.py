import sys
import math

def rad(r, i, e):
	pi = math.pi
	while r <= e:
		area = 4 * ((pi) * (r ** 2))
		volume = ((4 / 3) * (pi * (r ** 3)))
		print("{:>10.1f}{:>16.2f}{:>16.2f}".format(r, area, volume))
		r += i

def main():
	start_r = float(sys.argv[1])
	inc_r = float(sys.argv[2])
	end_r = float(sys.argv[3])

	h1 = "Radius (m)"
	h4 = "-" * len(h1)
	h2 = "Area (m^2)"
	h5 = "-" * len(h2)
	h3 = "Volume (m^3)"
	h6 = "-" * len(h3)

	print("{:>s} {:>15s} {:>15s}".format(h1, h2, h3))
	print("{:>s} {:>15s} {:>15s}".format(h4, h5, h6))
	rad(start_r, inc_r, end_r)

if __name__ == '__main__':
	main()