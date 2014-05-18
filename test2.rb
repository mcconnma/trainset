a = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2]
a = [1, 1, 2]

for i in 1..a.length
	res = a.permutation(i).to_a
	puts "#{res.length}"
	puts "#{res}"
end
