# Overall Design Notes

## General Purpose

To generate a suitable generic sleep-aid script for voice actors.

## How It Might Work

Use templates filled with either randomly-selected or weighted-choice content from a Json file to create a MarkDown file with a sleep-aid script. Certain perameters should be adjustable and batch-creation should be possible.

## Templates

While future iterations might include custom templates, initial designs should provide a simple output.

Jinja seems like the most established templating engine for future use but others may work better.

Databases might be useful in the future, but for now, JSON is fine.

## Script Attributes

 - Scripts should be at least 1000 words long but adjustable.
 - Scripts should include a licence header, title, and byline.
 - Scripts should be able to include a person's name for customisation.
 - Scripts should have an obvious opening section and closing section.

## First Task

Build a simple script generator capable of using content files to output an .md file.

## 10-to-1 section

Location / Theme (set) / Actions (set)