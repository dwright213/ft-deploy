# Flaschen-Taschen Deploy

#### Description:
A collection of Ansible stuff (playbooks, templates, etc) to set your Raspberry Pi up to be a Flaschen Taschen display server.


#### Reason for existence:
Because when you're monkeying around with a RPi (or multiple RPis) it's good to have a standard base configuration to work off of. The goal here is to streamline the setup for cases where there's multiple Raspbian installations and/or a developer is prone to rendering a Raspbian installation unbootable. 

Uses Ansible because I come from devops.


#### Requirements: 
Probably works with any Pi that Flaschen Taschen will run on, but here is what I'm using in my setup:

Two Raspberry Pi 3 B+ boards, connected through a gigabit switch to my router, one named "client", one named "server". Client exists to handle heavier graphic/video processing and if it dies, leave server doing it's thing. Server runs Raspbian Lite, Client runs Desktop Raspbian.


