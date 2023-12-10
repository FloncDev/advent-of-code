use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();

    let mut total = 0;
    let mut prev_total = 0;
    for line in input.lines() {
        let nums: Vec<i32> = line
            .split(" ")
            .into_iter()
            .map(|num| num.parse::<i32>().unwrap())
            .collect();

        let mut diffs = vec![nums.clone()];

        // The next vec of differences has to be 1 smaller than the previous
        for i in (0..nums.len()).rev() {
            let prev_diffs = &diffs[nums.len() - i - 1];
            let mut current_diffs = vec![];

            let mut previous = prev_diffs[0];
            for num in &prev_diffs[1..] {
                let diff = num - previous;
                current_diffs.push(diff);

                previous = num.to_owned();
            }

            diffs.push(current_diffs.clone());

            if current_diffs == vec![0; i] {
                break;
            }
        }

        // Predict the next numbers
        for i in (1..diffs.len() - 1).rev() {
            let next_diff = diffs[i].last().unwrap() + diffs[i - 1].last().unwrap();

            diffs[i - 1].push(next_diff);
        }

        for i in (1..diffs.len() - 1).rev() {
            let next_diff = diffs[i - 1][0] - diffs[i][0];

            // idk how to preappend
            diffs[i - 1].reverse();
            diffs[i - 1].push(next_diff);
            diffs[i - 1].reverse();
        }
        total += diffs[0].last().unwrap();
        prev_total += diffs[0][0];
    }

    println!("{}", total);
    println!("{}", prev_total);
}
