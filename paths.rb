
#b3={:name=>"-cl", :children=>[]}
#b2={:name=>"-s", :children=>[]}
#b1={:name=>"-cr", :children=>[]}

#a3={:name=>"-cl", :children=>[]}
#a2={:name=>"-s", :children=>[]}
#a1={:name=>"-cr", :children=>[b1,b2,b3]}

#a={:name=>"0", :children=>[a1,a2,a3]}

root={}
depth=2

def create(node)
	node = {:
	while depth != 0
		create(
	end

end

for d in 1..depth
	

end

for d in depth.downto(1)
	for n in 1..(3**d)
		x = "#{(64+d).chr}#{n}"
		puts "#{d}:#{x}"
		#instance_variable_set(x, {:name=>'x', :children=>[] })
	end
end

def paths(node,path='',&proc)
  if node[:children].empty?
    proc.call(path+node[:name])
  else
    node[:children].each{|c| paths(c,path+node[:name],&proc)}
  end
end

#paths(a){|path| puts path }
