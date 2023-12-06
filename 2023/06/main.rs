use regex::Regex;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();

    let re = Regex::new(r"\d+").unwrap();
    let lines: Vec<&str> = input.lines().collect();

    let times: Vec<i32> = re
        .find_iter(lines[0])
        .map(|i| i.as_str().parse::<i32>().unwrap())
        .collect();
    let distance: Vec<i32> = re
        .find_iter(lines[1])
        .map(|i| i.as_str().parse::<i32>().unwrap())
        .collect();

    let mut ways_to_beat = 1;

    for (time, distance_record) in times.iter().zip(distance.iter()) {
        let mut total_wins = 0;

        for speed in 0..=time.to_owned() {
            let distance = (time - speed) * speed;

            if distance > distance_record.to_owned() {
                total_wins += 1;
            }
        }

        ways_to_beat *= total_wins;
    }

    let large_time = times
        .clone()
        .iter()
        .map(|i| i.to_string())
        .collect::<Vec<String>>()
        .join("")
        .parse::<i64>()
        .unwrap();
    let large_distance = distance
        .clone()
        .iter()
        .map(|i| i.to_string())
        .collect::<Vec<String>>()
        .join("")
        .parse::<i64>()
        .unwrap();

    let mut ways_to_beat_large: i64 = 0;

    for speed in 0..=large_time {
        let distance = (large_time - speed) * speed;

        if distance > large_distance {
            ways_to_beat_large += 1;
        }
    }

    println!("{}", ways_to_beat);
    println!("{}", ways_to_beat_large);
}
