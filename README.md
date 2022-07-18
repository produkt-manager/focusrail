# focusrail
Prototype of a focus rail for macrophotography, using Sony Spresense® and Fischertechnik®.

## Sony Spresense

The Sony Spresense is a microcontroller device. It combines a small size with a huge performance, and a remarkable energy efficiency. The device and its ecosystem can be used for professional research and development. It is also very well suited to be employed in the fields of education, teaching and making.

Compared to other boards in the market, the Sony Spresense® is has a high degree of feature completeness, and it also includes very unique features for such a tiny-sized board. To be mentioned are for example its advanced audio capabilities or the ability to support GPS-based applications. 

A typical development setup includes the board itself, and the extension board. The extension board exposes the interfaces of the board to the outside world. Many use cases require a camera. Sony offers a corresponding solution that can be interfaced with the board.

Find here more specs about this interesting board and its ecosystem: https://github.com/produkt-manager/focusrail/blob/main/Literature.md

## Focusrail - Project

This project demonstrate a narrow application, that uses by far not the complete power and feature-richness of this board. However in its particular field of photography my prototype addresses and solves the common problem to create focus stacks.

## Macrophotography: The requirement

Both photography and videography cover a wide wide range of artistic genres. As a specialization, the macrophotography aims at tiny objects, such as insects, small parts or material surfaces. Some macro-photographers might even employ lenses that are usually found in microscopes. 

Macro photography comes with its own set of photographic and technical requirements. One common problem has to do with the limited depth of field of given lenses and cameras that are used for capturing macro photos.

### Technical process for macro photography

Modern photo- and videocameras or cameras on smartphones consist of an optical system and a sensor that captures the light that passes the optical system. These cameras also include the software that manages the capturing process, and all steps needed to pre- or post process the photograph („computational photography“).

The optical system has the task to collect the light-rays that are emitted by the scene to be captured, and it focusses these light rays towards a common focus-point. The focussed light rays pass the lens and the aperture before they hit a film (analog), or a camera sensor (digital). Either film or sensor records these light rays, and the result of this recording can then be seen as a photograph.

The optical system basically consists of these elements

- One or many lenses, that alter the direction of the incoming light rays. 
- An aperture that defines how many light rays can enter the camera body at the same time.
- A shutter that sits between lens and sensor and that defines the duration during which light reaches the sensor. The sensor has a defined light sensitivity (ISO-setting)
 
Depending on its sensitivity, the sensor makes sure that the photography is exposed correctly given aperture and shutter speed. At a given ISO setting, the aperture setting and the shutter speed correlate. Thereby a small aperture requires a large shutter speed, and vice versa. On the other hand the aperture also correlate to the depth of field (DOF), and therefore the distance range in which the object is in focus. Here small apertures correspond to a small DOF, and large apertures correspond to a large DOF.

Due to technical limitations, macro photos are typically characterized by a shallow depth of field. Therefore given the light conditions only parts of the object of interest are sharp, while areas in front or behind the focus point are blurred. In order to create photos that are completely in focus, the photographer typically employs a technology that is called focus stacking.

### Focus stacking

At a given setting for aperture, ISO, and shutter speed only a slice of the object is in focus. In order to extend the focus area, the photographer can capture multiple photographs of the same scene, while he makes sure that each time a different plane of the photo is in focus. In the post processing step these multiple photographs, and manly the in-focus areas of each of them are then stacked onto each other using a proper algorithm. At the end the in-focus areas of all images are combined in one image.

In an earlier project, I have tested stacking algorithms, and have programmed corresponding prototypes. See https://github.com/produkt-manager/focusstacking for more information.

Task of the actual project is to create the mentioned stack of photos. The options are (all other parameters remain unchanged):

- Alter the object-lens-distance in steps, while you take a photograph after each step.
- Alter the lens-sensor-distance in steps, while you take a photograph after each step.

The second option requires a fundamental change in the camera itself, while the first method only requires that you move the complete camera in steps, while you leave all settings unchanged. Therefore most devices mechanically effect the  object-lens-distance. To achieve this, the camera and the lens is typically mounted to a focus rail, while a motor takes care that the camera is moved in steps towards the object.

Such a device typically consist of mechanical parts (focus rail), electronics (motor control), and software that is capable to interface and affect the motor and the shutter of the camera.

### Fischertechnik

Fischertechnik® is prototyping system that aims both kids, and educated engineers the like. Similar to the competing Lego® system it supports a large area of technical applications, such as mechanics, pneumatics, dynamics, electronic, or robotics, to name just a few. The normed parts allow the user to construct a wide variety of machines and devices, and also supports motor control.

In this project I will use Fischertechnik® in order to build the prototype of a motorized focus rail. In this setup the Sony Spresense is equipped with a camera board, and is mounted to this focus rail. The board interfaces to the Fischertechnik® motorcontroller, which is in charge of the motor movement. The software on the Sony Spresense will control the motorcontroller, while it captures the photos. These stacks are lateron combined into one photo.

The following literature is helpful to understand the creation and control of robots using Fischertechnik®: https://github.com/produkt-manager/focusrail/blob/main/Literature.md

h1. Implementation


--- 
Disclaimer: I do not take responsibility for the content of external websites.
Copyright 2022 Andreas Rudolph, and is released under the Apache 2.0 license (see license file).
