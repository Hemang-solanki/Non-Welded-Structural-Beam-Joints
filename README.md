# Modular I-beams Connections (No Welding)

This repository documents my 2021 entry for a design challenge focused on **rapid construction of buildings without the need for welding**. The goal was to find structural connection methods that are strong, modular, and easy to assemble/disassemble in the field. Although this project did not win the challenge, it represents an alternative approach to connecting beams securely while maintaining flexibility in construction. This beam system has never been 3D printed or physically tested; it exists only as a concept, designed and modeled digitally. I am curious whether a 3D print would function as intended.

## Concept

The system relies on **custom 3D-printed connectors** and mechanical fasteners (i.e. the cross-shaped clamps) that allow I-beams and other structural members to be joined quickly. The connectors are designed to lock beams together from multiple directions, providing stability without welding. Also, the assembly relies on gravity, as the cross-shaped clamps are designed to self-lock and secure the beams in place without additional welding.

- Rapid assembly/disassembly  
- No specialized welding equipment required  
- Modular and reusable components  

## 3D Models

The system is designed to join <i>I-beams</i> and <i>perforated plates</i> without welding, relying instead on custom <i>connectors</i> that slot into place. The main innovation is the <i>cross-shaped clamp</i> that uses gravity and geometry to achieve a <b>self-locking effect</b>. The structure is composed of <i>I-beams</i> which form the load-bearing skeleton, <i>perforated plates</i> that act as mounting interfaces, <i>cross-shaped clamps</i> that accept beams from multiple directions and lock them together, and <i>support wedges or pads</i> that secure alignment. The mounting principle is simple: the base beams are placed horizontally, then the cross clamp is positioned at the intersection where beams will meet. Each beam is slid into the clamp slots, where the rectangular openings align them automatically.

<div align="center">
  <img src="https://github.com/Gagniuc/Non-Welded-Structural-Beam-Joints/blob/main/img/abstract-side.png" alt="beam">
</div>

As the beams settle under their own weight, gravity presses them into the connector and the cross geometry prevents lateral movement, creating a <b>self-locking joint</b>. Once the base is stabilized, vertical supports can be added in the same way, using additional clamps at higher levels. The perforated plates allow optional bolting if extra rigidity is needed, but the system is intended to function as a weld-free and tool-minimal solution. In this way, the assembly relies on <i>gravity</i> and <i>geometric interlocking</i>, with distributed contact surfaces that spread loads evenly instead of concentrating stress on a single welded joint.  

## Original Models on Tinkercad

You can view and interact with the original 3D designs directly on Tinkercad:

- [Beam Binding Mod 1](https://www.tinkercad.com/things/8ZvYYCPgAwp-gagniuc-beam-binding-mod-1)  
- [Beam Binding Mod 2](https://www.tinkercad.com/things/acZ6fLl6scF-gagniuc-beam-binding-mod-2)  
- [Beam Binding Mod 3](https://www.tinkercad.com/things/ae3SANVkH5d-gagniuc-beam-binding-mod-3)  
- [Beam Binding Mod 4](https://www.tinkercad.com/things/hHmCYtFYW13-gagniuc-beam-binding-mod-4)


### Assembly Procedure  

<i>Step 1 – Positioning the connector</i>  
Place the cruciform connector at the intended joint location. The connector is oriented so that its protrusions align with the perforation grid of the beams.  

<i>Step 2 – Inserting the vertical member</i>  
Insert the perforated I-section vertically into the central cavity of the connector. The geometry guides the profile into position, and gravity ensures the element seats itself in a self-locking manner.  

<div align="center">
  <img src="https://github.com/Gagniuc/Non-Welded-Structural-Beam-Joints/blob/main/img/pole-out.gif" alt="beam">
</div>

<i>Step 3 – Engaging horizontal beams</i>  
Slide horizontal perforated I-beams into the lateral openings of the connector. The protrusions of the connector engage with the cross-shaped perforations, preventing both translation and rotation of the beams.  

<div align="center">
  <img src="https://github.com/Gagniuc/Non-Welded-Structural-Beam-Joints/blob/main/img/beam-in.gif" alt="beam">
</div>

<i>Step 4 – Ensuring alignment</i>  
Verify that all protrusions are fully seated in the beam perforations. This guarantees that the load transfer occurs through direct bearing and geometric interlock.  

<i>Step 5 – Repetition and boundary nodes</i>  
Repeat the process for adjacent axes. At corner or boundary nodes, only the available faces of the connector are used, leaving some protrusions unengaged.  

<div align="center">
  <img src="https://github.com/Gagniuc/Non-Welded-Structural-Beam-Joints/blob/main/img/rotate.gif" alt="beam">
</div>

<i>Step 6 – Disassembly</i>  
The system can be dismantled by lifting the connector vertically off the column or sliding out the horizontal beams. The process is fully reversible and requires no welding or specialized tools.  

<div align="center">
  <img src="https://github.com/Gagniuc/Non-Welded-Structural-Beam-Joints/blob/main/img/pole-in.gif" alt="beam">
</div>

---

## Assembly Principle  

The mounting process is based on <b>gravity</b> and <b>geometry</b>:  
- <b>Gravity</b> presses the beams downward into the clamps.  
- <b>Cross-shaped clamp geometry</b> ensures beams self-lock at 90° intersections.  
- <b>Perforated plates</b> provide flexibility for reinforcement without welding.  

---

## Status

This is a **conceptual project** and not yet tested in real-world construction. It is shared here as a resource and inspiration for further exploration of **modular building techniques**. Moreover, this system has <b>never been 3D printed, molded and physically tested</b>; it exists only as a concept, designed and modeled digitally. I am curious whether a real 3D print would function <i>as intended</i>.  

---
*Created in 2021 as part of a rapid construction challenge.*
