# data.py is responsible for storing explanations, questions, settings and sample responses in dictionaries for easy access throughout the program.

user = {
  "name": "John",
  "level": {
    'A': 1,
    'B': 1,
    'C': 1,
    'D': 1,
    'E': 1
  },
  "beginner": True,
  "correct": 0,
  "incorrect": 0
}

settings = {
  "instant_eddie": 0.01,
  "opt1": "OFF",
  "eddie_hints": 10,
  "opt2": "ON"
}

try_again = [
  "Not quite, have another try.", "Oops! You made a mistake. Try again.",
  "That's incorrect. Try again."
]

correct = [
  "Correctamundo!", "That's right!", "Good one!", "Great job!", "Nice!",
  "Great work!", "That's correct!", "Correct. Keep it up!"
]

congratulations = ["Great job!", "Nice work!", "Great work!", "Keep it up!"]

try_limit = [
  "Nooo, your 3 tries are up.", "Ahh, you reached the answer limit.",
  "Nooo, you reached the answer limit.", "Ahh, your 3 tries are up.",
  "Oops, your 3 tries are up.", "Oops, you reached the answer limit."
]

eddie_speech = {
  "hints": [
    "\x1B[3mMake sure to read the question carefully! - Eddie\x1B[0m",
    "\x1B[3mTop Tip: You've got this! - Eddie\x1B[0m",
    "\x1B[3mHave a think back to the lesson - Eddie\x1B[0m"
  ],
  "encouragement": [
    "\x1B[3mNo need to stress! Everyone makes mistakes sometimes. - Eddie\x1B[0m",
    "\x1B[3mTop Tip: You've got this! - Eddie\x1B[0m",
    "\x1B[3mPractice makes permanent! - Eddie\x1B[0m"
  ]
}

# contains each topic for each module
explanations = {
  'A': {
    1:
    "Algebra is a branch of mathematics that deals with the study of numbers and their properties. It involves using letters or symbols, called pronumerals, to represent numbers that we don't know yet. These letters or symbols are used to write algebraic expressions (eg. 5a + 2) and equations (eg. 2 + a = b) that help us solve problems.\n\nIn algebra, we use terms to describe the parts of an expression that are separated by + or -, for example '5a'. The number that is attached to a pronumeral is called a coefficient. We can use these terms, pronumerals, and coefficients to write our own algebraic expressions.",
    2:
    "To simplify algebraic expressions, there are a few key steps to follow. Firstly, we need to identify any like terms - these are terms that have the same variable and exponent (eg. 5x and 2x, 3a² and -6a²). We can then combine these terms by adding or subtracting their coefficients. For example, 3y - 5y becomes -2y. \n\nWe can also simplify expressions by using the order of operations - this means performing any calculations inside parentheses first, then any exponents, then multiplication or division from left to right, and finally addition or subtraction from left to right. Complete the BODMAS lesson in order to understand this better. If a variable is given, swap it out for the number and calculate the answer. Following these steps can help us to simplify algebraic expressions and make them easier to understand.\n\nExample:\n\nSimplify 5 - 2a³ + 8a³ x 6\n= 5 - 2a³ + 42a³\n= 5 - 44a³",
    3:
    "Solving a linear equation involves finding the value of the unknown variable that makes the equation true. Here are the steps to solve a linear equation: \n\n1. Identify the variable in the equation. This is usually represented by a letter, such as x or y.\n\n2. Simplify the equation by combining like terms on each side of the equation. For example, if the equation is 2x + 3 = 7x - 5, you can simplify it by subtracting 2x from both sides to get 3 = 5x - 5.\n\n3. Isolate the variable on one side of the equation. To do this, you can add or subtract terms from both sides of the equation until only the variable remains on one side. For example, if the equation is 3 = 5x - 5, you can add 5 to both sides to get 8 = 5x.\n\n4. Solve for the variable by dividing both sides by the coefficient (number in front of the variable). For example, if the equation is 8 = 5x, you can divide both sides by 5 to get x = 8/5.\n\n5. Check your answer by plugging it back into the original equation. If the equation is true when you substitute the value for the variable, then you have solved the equation correctly.\n\nSo, in summary, the steps to solve a linear equation are to identify the variable, simplify the equation, isolate the variable on one side, solve for the variable, and check your answer."
  },
  'B': {
    1:
    "An angle is the space between two intersecting lines or surfaces, measured in degrees or radians. Angles are all around us, from the corners of your classroom to the angles of your fingers. Understanding angles is an essential skill in mathematics, as it helps us to measure and describe shapes and objects accurately.\n\nThere are five main types of angles: acute, right, obtuse, straight, and reflex. An acute angle measures less than 90 degrees, a right angle measures exactly 90 degrees, and an obtuse angle measures greater than 90 degrees but less than 180 degrees. A straight angle measures exactly 180 degrees, and a reflex angle measures greater than 180 degrees but less than 360 degrees.",
    2:
    "Different shapes have different angle properties. In a triangle, the sum of the three angles is always 180 degrees, and each angle is denoted by a Greek letter. In a square, each angle measures 90 degrees, making it a right angle. Other polygons such as rectangles, pentagons, and hexagons also have specific angle measurements that determine their shape and properties. Understanding the angles in a shape is essential in solving problems related to area, perimeter, and other geometric properties."
  },
  'C': {
    1:
    "BODMAS is a way to remember the order of operations when solving mathematical expressions. It stands for:\n\nB - Brackets first\nO - Orders (ie Powers and Square Roots, etc.)\nDM - Division and Multiplication (left-to-right)\nAS - Addition and Subtraction (left-to-right)\n\nThis means that when solving an expression, you first simplify any expressions inside brackets, then evaluate any powers or roots, then perform any multiplication or division in order from left to right, and finally perform any addition or subtraction in order from left to right. Remembering the order of operations is important for solving mathematical expressions accurately."
  },
  'D': {
    1:
    "Area and perimeter are two important concepts in geometry. The perimeter of a shape is the total length of its sides. To find the perimeter of a shape, you add up the length of all of its sides. The area of a shape is the amount of space inside it. To find the area of a shape, you multiply its length by its width (for a rectangle) or use an appropriate formula for other shapes such as triangles or circles. \n\nIt's important to remember that the units of measurement for area and perimeter are different. Perimeter is measured in linear units such as centimeters or meters, while area is measured in square units such as square centimeters or square meters. Understanding the difference between area and perimeter is essential in many areas of mathematics and real-world applications, such as measuring the dimensions of a room or calculating the amount of material needed to cover a surface.",
    2:
    "The perimeter of a circle is a fundamental concept in geometry that refers to the distance around the edge of a circle. It is also known as the circumference of the circle. The formula for calculating the perimeter of a circle is 2πr, where r is the radius of the circle and π (pi) is a mathematical constant approximately equal to 3.14. In other words, the perimeter of a circle can be found by multiplying the diameter of the circle by pi. The perimeter of a circle is an important property in many real-world applications, such as calculating the distance around a circular track or the length of a cable required to wrap around a circular object.",
    3:
    "Area formulas are mathematical expressions used to calculate the total amount of space occupied by a two-dimensional shape. The formula for finding the area of a shape depends on its specific properties. For example, the area of a rectangle can be calculated by multiplying its length by its width, while the area of a triangle can be calculated using the formula (base x height)/2. Similarly, the area of a circle can be calculated using the formula πr^2, where r is the radius of the circle and π is a mathematical constant approximately equal to 3.14. Understanding area formulas is essential in solving problems related to geometry and measurements, such as calculating the amount of carpet required for a room or the area of a field for farming."
  },
  'E': {
    1:
    "Pythagoras' theorem is a fundamental concept in mathematics that describes the relationship between the sides of a right-angled triangle. According to the theorem, the square of the length of the hypotenuse (the longest side) of a right-angled triangle is equal to the sum of the squares of the lengths of the other two sides. In mathematical notation, this can be expressed as a² + b² = c², where a and b are the lengths of the two shorter sides, and c is the length of the hypotenuse. Pythagoras' theorem is used extensively in mathematics and engineering, and it has a wide range of practical applications, such as in architecture, surveying, and navigation.",
    2:
    "To use Pythagoras' theorem to find a side that isn't the hypotenuse of a right-angled triangle, you first need to identify which sides are the hypotenuse and which ones are the other two sides. Once you have done this, you can use the formula a^2 + b^2 = c^2, where a and b are the lengths of the two shorter sides, and c is the length of the hypotenuse.\n\nSuppose you want to find the length of one of the shorter sides, say a, and you know the lengths of the other shorter side, b, and the hypotenuse, c. To do this, you can rearrange the formula a^2 = c^2 - b^2, so that a is isolated on one side of the equation. Then, you can take the square root of both sides to find the length of a."
  }
}

# contains questions for every level of every topic. format: question, answer
# data types: strings, characters, integers and floats
questions = {
  'A': {
    1: {
      "How many terms are in the expression \x1B[3m3a + b + 13c\x1B[0m?": 3,
      "What is the coefficient of \x1B[3m4c\x1B[0m?": 4,
      "What is the pronumeral in \x1B[3m5k\x1B[0m?": "k",
      "Is \x1B[3mm - 3\x1B[0m an equation?": "no",
      "Write an expression for \x1B[3mp plus q\x1B[0m": "p + q"
    },
    2: {
      "Simplify 2a + a.": "3a",
      "Simpify 3w - 8w.": "-5w",
      "If x = 3, simplify the expression 2x + 5.": 11,
      "Simplify 10c² + 5 + 2c² - 11": "12c - 6",
      "If x = -1, simplify the expression 4 x 2b² + 13 - 2c²": 19
    },
    3: {
      "If x + 1 = 5, what does x equal.":
      4,
      "If 2a - 1 = 9, what does a equal":
      5,
      "Solve the equation 5x - 7 = 13. Write in the form 'x = ?'":
      "x = 4",
      "Solve the equation 9b + 10 = 13. Write in the form 'b = ?' and give your answer correct to 1 decimal place.":
      0.3
    }
  },
  'B': {
    1: {
      "What angle is less than 90°?":
      "acute",
      "Is 125° a reflex angle?":
      "no",
      """What type of angle is this?                                                                         
      @(                                                                        
        @(                                                                      
         &@                                                                     
          .@,                                                                   
            @@                                                                  
             /@.                                                                
               @%                                                               
                %@                                                              
                 .@/                                                            
                   @@                                                           
                    *@.                                                         
                      @@&,                                                  
                       (@                                                   
                         @(                                                  
                          &@                                                 
                           .@(//////////@@//////////////////////////////""":
      "obtuse",
      "How many degrees are in a right angle?":
      "90",
      "Can a right angle be classified as obtuse?":
      "no"
    },
    2: {
      "How many degrees are in a triangle?": 180,
      "What about in a square?": 360,
      "If one angle of a triangle is 60 degrees, what do the other two add up to?": 120,
      "The sum of all in the angles in n squares is 2520°. Find n": 7,
      "The smallest angle in an isosceles triangle is 20°. How many degrees are in the largest angle?": 80
    }
  },
  'C': {
    1: {
      "What comes first, () or +-": "()",
      "What does the O in BODMAS stand for?": "order",
      "Solve 5 + 4 x 6": 29,
      "Solve -1 x (6 + 2) x 9": -72,
      "Solve (12 + 7) x 11 - 11 + 1": 199
    }
  },
  'D': {
    1: {
      "Can perimeter be measured in km?": "yes",
      "Can area be measured in miles?": "no",
      "How many cm is the perimeter of a square with side length 10cm?": 40,
      "How many km² is the area of a 5km by 4km field?": 20,
      "True or False: A rectangular garden measures 20m by 30m. It has a perimeter of 100m": "true"
    },
    2: {
      "What do we call the distance from the center of a circle to the outside?": "radius",
      "True or False: The radius is double the diameter.": "false",
      "What is this symbol called: π": "pi",
      "What is the circumference of a circle with radius 5m? Give your answer to 1 decimal place.": 15.7
    },
    3: {
      "Challenge Question: The area formula for a trapezium can be written as 0.5 x h x (a + b). Is this true or false?": "true"
    }
  },
  'E': {
    1: {
      "What is the name of the longest side in a right angled triangle?":
      "hypotenuse",
      "A right-angled triangle has sides of length 7 cm and 24 cm. What is the length of the hypotenuse?":
      25,
      "If a right-angled triangle has sides of length 6 cm and 8 cm, what is the length of the hypotenuse?":
      10,
      "A rectangular garden has dimensions of 5 metres by 12 metres. What is the diagonal distance from one corner of the garden to the opposite corner?":
      13
    },
    2: {
      "If a right-angled triangle has a hypotenuse of length 13 units and one shorter side of length 5 units, what is the length of the other shorter side?":
      12,
      "A ladder is leaning against a wall at a 60-degree angle. The ladder is 10 meters long, and its foot is 4 meters away from the wall. What is the height of the ladder on the wall? Give your answer to the nearest metre.":
      9,
      "A right-angled triangle has sides of length 5 cm and 12 cm. What is the length of the shorter side adjacent to the 5 cm side? Give your answer to 1 decimal place.":
      10.9,
      "A 6m tall pole is standing vertically on level ground. The pole is anchored to the ground with a rope that extends from the top of the pole to the ground. The rope is 15 meters long. How far from the base of the pole is the rope anchored to the ground? Give your answer to 1 decimal place.":
      13.7
    }
  }
}
