use std::{
    collections::HashMap,
    io::{self, Read},
};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();

    let str_digits_map: HashMap<&str, i32> = HashMap::from([
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9),
    ]);
    let str_digits: Vec<&str> = "one two three four five six seven eight nine"
        .split(" ")
        .collect();

    let mut total = 0;
    let mut total2 = 0;

    for line in input.lines() {
        let chars: Vec<char> = line.chars().collect();

        // Basically does the following:
        // 1 2 3 4 5
        // ^ ----- ^
        // and they carry on going until they are on the opposite side
        // of where they started

        let mut calibration_value = 0;
        for (left, right) in chars.clone().iter().zip(chars.iter().rev()) {
            if calibration_value < 10 && left.is_numeric() {
                calibration_value += left.to_string().parse::<i32>().unwrap() * 10;
            }

            if calibration_value % 10 == 0 && right.is_numeric() {
                calibration_value += right.to_string().parse::<i32>().unwrap();
            }
        }

        total += calibration_value;

        let mut calibration_value = 0;
        let mut found = [false, false];

        for i in 0..line.len() {
            let right = line.len() - i - 1;
            if !found[0] {
                if chars[i].is_numeric() {
                    calibration_value += chars[i].to_string().parse::<i32>().unwrap() * 10;
                    found[0] = true
                } else {
                    let start = &line[i..line.len()];
                    for num in &str_digits {
                        if start.starts_with(num) {
                            calibration_value += str_digits_map.get(num).unwrap() * 10;
                            found[0] = true;
                        }
                    }
                }
            }

            if !found[1] {
                // Right not found
                if chars[right].is_numeric() {
                    calibration_value += chars[right].to_string().parse::<i32>().unwrap();
                    found[1] = true;
                } else {
                    let end = &line[right..line.len()];
                    for num in &str_digits {
                        if end.starts_with(num) {
                            calibration_value += str_digits_map.get(num).unwrap();
                            found[1] = true;
                        }
                    }
                }
            }
        }

        total2 += calibration_value;
    }

    println!("{}\n{}", total, total2);
}
