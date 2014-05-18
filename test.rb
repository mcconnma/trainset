def subset_sum(numbers, target, partial=[])
  s = partial.inject 0, :+
	# check if the partial sum is equals to target

  puts "sum(#{partial})=#{target}" if s == target

  return if s >= target # if we reach the number why bother to continue

  (0..(numbers.length - 1)).each do |i|
    n = numbers[i]
    remaining = numbers.drop(i+1)
    subset_sum(remaining, target, partial + [n])
  end
end

#subset_sum([3,9,8,4,5,7,10],15)
#subset_sum([1,2,3,4,5,6,7,8,9,10],100000)
start = [1,2,3,4,5,6,7,8,9,10]
puts start.to_s
subset_sum(start,10)
