# make your program below
require "http"
quit = false
search = true


while !quit
  quit2 = false

  if search
    puts "What subreddit would you like to visit?"
    url_input = gets.chomp
    puts "_____________________________________________"

    subreddit_response = HTTP.get("https://www.reddit.com/r/#{url_input}/.json")

    subreddit_data = subreddit_response.parse(:json)
    subreddit_content = subreddit_data["data"]["children"]
    #p subreddit_content.length
  end

  index = 0
  while index < subreddit_content.length
    post_data = subreddit_content[index]["data"]
    if post_data["post_hint"] == "image"
      is_image = true
      address = post_data["thumbnail"]
      result = `python3 ascii-art-maker.py #{address}`
    else
      is_image = false
    end

    puts "_____________________________________________"
    puts
    puts "#{index +1}: #{post_data["title"]}"
    puts "        Author: u/#{post_data["author"]}"
    puts "        Upvotes: #{post_data["ups"]}"
    puts
    
    if is_image
      image_display = File.read("ascii_image.txt")
      puts image_display
    end

    puts "Type [#{index +1}] to view comments. (#{post_data["num_comments"]})" 
    puts
    

    index += 1
  end

  while !quit2
    quit3 = false
    puts
    puts "_____________________________________________"
    puts "Enter a comment section, or enter [q] to quit, or enter [s] to search a new subreddit."
    puts
    input = gets.chomp
    puts "_____________________________________________"
    if input == "q"
      quit2 = true
      quit = true
    elsif input.to_i.to_s == input && input.to_i <= subreddit_content.length + 1

      while !quit3
        quit4 = false
        index = input.to_i - 1
        comment_address = subreddit_content[index]["data"]["permalink"]
        comment_response = HTTP.get("https://www.reddit.com#{comment_address}.json")
        comment_data = comment_response.parse[1]["data"]["children"]
        
        comment_data.each do |comment|
          author = comment["data"]["author"]
          body = comment["data"]["body"]
          puts "         Author: #{author}"
          puts body
          puts
        end

        while !quit4
          puts
          puts "_____________________________________________"
          puts "Enter [b] to go back, or enter  [q] to quit, or enter [s] to search a new subreddit."
          puts "_____________________________________________"
          puts
          comment_input = gets.chomp

          if comment_input == "b"
            quit4 = true
            quit3 = true
            quit2 = true
            search = false

          elsif comment_input == "q"
            quit4 = true
            quit3 = true
            quit2 = true
            quit = true
          elsif comment_input == "s"
            quit4 = true
            quit3 = true
            quit2 = true
            search = true
          end

        end
        quit3 = true
      end

      quit2 = true
    elsif input == "s"
      quit2 = true

    end


  end
  
end