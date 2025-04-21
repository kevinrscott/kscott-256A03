# Event Registration System - Django App

**ITAS256 - Assignment 3<br>
Kevin Scott**

## Overview

This is a Django-based event registration system that allows users to manage and register for events.
It comes with two different roles - Administrator, and Registrant, each have different permissions and functionality.

## Features

### Accounts

- Registrants can create an account
- Both roles can log in and log out
- Admin accounts must be pre-made
- Validation
  - Username must be an email
  - Password must be 6+ characters contain a number, uppercase, and lowercase

### Events

- Both roles can search for events by name
- Administrators:
  - Create, update, and delete events
  - View all events
- Registrants: 
  - Register/Unregister from events
  - View upcoming events and events registered for

### Reports

- Administrators:
  - View a list of all users with username, name, and role
  - View a list of all events and the registrants for it
