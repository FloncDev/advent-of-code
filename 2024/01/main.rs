use std::io::{self, Read};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;

    let mut left: Vec<i32> = vec![];
    let mut right: Vec<i32> = vec![];

    for line in input.lines() {
        let mut values = line.split_whitespace();

        left.push(values.next().unwrap().parse()?);
        right.push(values.next().unwrap().parse()?)
    }

    let mut total_distance = 0;

    left.sort();
    right.sort();

    for (left, right) in left.clone().into_iter().zip(&right) {
        total_distance += (left - right).abs();
    }

    let mut similarity = 0;

    for left in &left {
        similarity += right.iter().filter(|x| x == &left).count() as i32 * left;
    }

    println!("{} {}", total_distance, similarity);

    Ok(())
}
