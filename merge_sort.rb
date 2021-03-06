require 'pry'

def mergesort(arr)
	puts "splitting #{arr}"
	return arr if arr.length == 1
	mid = arr.length/2
	l = mergesort(arr[0...mid])
	r = mergesort(arr[mid..-1])
	merge(l,r)
end

def merge(l,r)
	i = 0
	j = 0
	result = []
	while i <= l.length - 1 && j <= r.length - 1 do
		if l[i] < r[j]
			result << l[i]
			i += 1
		else
			result << r[j]
			j += 1
		end
	end
	if i != l.length
		puts "merging #{result + l[i..-1]}"
		return result + l[i..-1]
	end
	if j != r.length
		puts "merging #{result + r[j..-1]}"
		return result + r[j..-1]
	end
end

p mergesort([7,1,4,6,2])
