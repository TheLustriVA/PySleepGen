# Overall Design Notes

## General Purpose

To generate a suitable generic sleep-aid script for voice actors.

## How It Might Work

Use templates filled with either randomly-selected or weighted-choice content from a Json file to create a MarkDown file with a sleep-aid script. Certain perameters should be adjustable and batch-creation should be possible.

## Templates

While future iterations might include custom templates, initial designs should provide a simple output.

Jinja seems like the most established templating engine for future use but others may work better.

Databases might be useful in the future, but for now, JSON is fine.

## Types of script

 - Guided: A guided sleep aid where the narrator is simply being themselves and talking directly to the listener
 - Acted: A sleep aid where the narrator is playing a charactor and the language is less direct, like talking a child or friend to sleep.

## Script Attributes

 - Scripts should be at least 1000 words long but adjustable.
 - Scripts should include a licence header, title, and byline.
 - Scripts should be able to include a person's name for customisation.
 - Scripts should have an obvious opening section and closing section.

## First Task

Build a simple script generator capable of using content files to output an .md file.

## 10-to-1 section

Location / Theme (set) / Actions (set)

### Countdown Example

Ten

1)) <<You close your eyes if you haven't already.>> (variations on closing eyes/headphones)

2)) <<Find a position for your body that allows you to let go of your muscles>> (variations on getting into position)

3)) <<Take a minute to sort yourself out and become as comfortable as possible>> (variations on getting your clothes/glasses/blankets in order)

Nine

4)) <<The colours and shapes behind your closed eyes lose focus as you begin to imagine yourself>> (variations on transition from waking to fantasising)
5)) <<standing on a white-sand beach with brilliant blue water fringed by lightly-breaking waves>> (variations on establishing the setting)

Eight

6)) <<The sounds of breaking waves and wind across the sand refreshes you>> (variations on positive feelings from setting)
7)) <<You look around to see the beach extends as far as you can see in both directions>> (variations on deliberate sensory search)

Seven

8)) <<You feel a gentle urge to walk westward along the beach>> (variations on first motive to act)
9)) <<Your heart lightening and filling with joy as you let the sea air wash over you>> (variations on reward for acting)

Six

10) <<A small crab makes its way up the beach in your direction, pausing to take a look at you>> (variations on the introduction of a benevolent entity)
11) <<You wave at it and smile. A moment later, you swear you can see the crab wave its claw back at you>> (variations on fantastic introductions)

Five

12) <<You continue along the beach, the small crab waddling alongside you, stopping occassionaly to inspect a shell or pebble>> (variations on cute occassion to deepen dream-thinking)
12) <<The waves rush up the shore toward you, but your feet stay dry as the water seems to avoid your feet>> (variations on cute occassion to deepen dream-thinking)

Four

13) <<You come across a rocky outcropping and a pool of clear water where a nearby creen runs into the ocean>> (variations on finding comfortable place to rest)
14) <<The water is the perfect temperature as you lower yourself into the bubbling clear pool>> (variations on committing to comfortable place to rest)

Three

15) <<Your muscles relax completely as you give yourself over to the pool>> (variations on increased calm from comfortable place to rest)
15) <<You find a place to rest and feel relaxation spreading up from your toes, through your legs, your torso, your arms, and neck>> (variations on increased calm from comfortable place to rest)

Two

16) <<You feel yourself melt into the rocks, the sand, and the water around you.>> (variations on falling asleep in fantasy)
16) <<Your breathing deepens and slows to take on the rhythm of the surf nearby.>> (variations on falling asleep in fantasy)

One

17) <<Your entire body is now at peace, relaxed into the soft land of sleep>> (variations on confirming that your body is asleep)
17) <<Every cell in your body floats in a deep world of slumber>> (variations on confirming your body is asleep)