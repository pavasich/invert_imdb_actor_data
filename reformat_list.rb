require 'json'

file = File.read('movie_to_actor.json')

data_hash = JSON.parse(file)

new_db = []

data_hash.each do |movie, data|
  title = ''
  year = ''
  cast = []
  if movie.is_a? String
    title = movie.split('(')[0].strip
    year = movie.split('(')[1]
    if year.is_a? String
      year = year.split(')')[0]
    end
  end
  if data["actors"].is_a? Array
    cast = data["actors"]
  end
  movie_data = {
    :title => title,
    :year => year,
    :full_cast => cast
  }
  new_db.push movie_data
end

File.open("full_cast_db.json","w") do |f|
  f.write(JSON.pretty_generate(new_db))
end
