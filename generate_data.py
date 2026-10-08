import numpy as np
import pandas as pd


# Reproducible dataset
np.random.seed(55)

N = 1200

counties = [
    "Nairobi",
    "Nakuru",
    "Kisumu",
    "Mombasa",
    "Laikipia",
]

genders = ["Female", "Male"]

school_types = ["Public", "Private"]


# Basic learner characteristics
student_id = np.arange(1, N + 1)

gender = np.random.choice(
    genders,
    size=N,
    p=[0.52, 0.48]
)

school_type = np.random.choice(
    school_types,
    size=N,
    p=[0.70, 0.30]
)

county = np.random.choice(
    counties,
    size=N,
    p=[0.25, 0.20, 0.20, 0.20, 0.15]
)


# Attendance percentage
attendance = np.clip(
    np.random.normal(82, 9, N),
    50,
    100
).round(1)


# Study hours per week
study_hours = np.clip(
    np.random.normal(10, 4, N),
    1,
    25
).round(1)


# Subject scores
school_effect = np.where(school_type == "Private", 4, 0)

attendance_effect = (attendance - 75) * 0.20

study_effect = study_hours * 1.2

noise_math = np.random.normal(0, 8, N)
noise_english = np.random.normal(0, 8, N)
noise_science = np.random.normal(0, 8, N)


math_score = np.clip(
    48
    + study_effect
    + attendance_effect
    + school_effect
    + noise_math,
    0,
    100
).round(1)


english_score = np.clip(
    52
    + study_effect * 0.90
    + attendance_effect
    + school_effect
    + noise_english,
    0,
    100
).round(1)


science_score = np.clip(
    47
    + study_effect * 1.05
    + attendance_effect
    + school_effect
    + noise_science,
    0,
    100
).round(1)


# Build dataframe
df = pd.DataFrame({
    "student_id": student_id,
    "gender": gender,
    "school_type": school_type,
    "county": county,
    "attendance": attendance,
    "study_hours": study_hours,
    "math_score": math_score,
    "english_score": english_score,
    "science_score": science_score,
})


# Save dataset
df.to_csv("student_performance.csv", index=False)


print("=" * 60)
print("STUDENT PERFORMANCE DATA GENERATION COMPLETE")
print("=" * 60)
print(f"Students generated: {len(df)}")
print("Seed: 55")
print("File: student_performance.csv")
print("=" * 60)