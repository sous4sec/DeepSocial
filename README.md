# DeepSocial - Social Media Profile Researcher

![image](https://github.com/user-attachments/assets/1e4f6b9e-623d-499c-9400-82660ac98a57)


DeepSocial is a Python-based tool that allows you to search for user profiles across various social media platforms, online stores, work platforms, streaming services, and even hacking sites. With DeepSocial, you can quickly gather information about an individual's online presence and explore their profiles across different networks.

## Features
- Search multiple platforms like Twitter, Instagram, LinkedIn, YouTube, and many others.
- Check user availability on online stores like eBay, Amazon, Etsy, and more.
- Explore work and freelancing platforms such as Upwork, Fiverr, and Freelancer.
- Verify profiles on streaming services like Spotify, SoundCloud, and YouTube Music.
- Find users on hacking-related sites like Hack The Box, TryHackMe, and VulnHub.

## Installation
To install the DeepSocial tool, clone this repository to your local machine:

```bash
git clone https://github.com/sous4sec/DeepSocial.git
cd DeepSocial
```

Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

## Usage
After installing the required dependencies, you can run the script to search for a user profile. The basic command syntax is:

```bash
python DeepSocial.py <username> [--c {all,sm,s,w,st,ht}]
```

- `<username>` is the username you want to search for across various platforms.
- `--c` allows you to specify the categories to search in:
  - `all`: Search all categories (default).
  - `sm`: Search only on social media platforms.
  - `s`: Search only in online stores.
  - `w`: Search only in work platforms.
  - `st`: Search only in streaming platforms.
  - `ht`: Search only in hacking-related sites.

### Example
To search for the user `john_doe` across all categories, run:

```bash
python DeepSocial.py john_doe --c all
```

To search for the user `john_doe` only on social media platforms:

```bash
python DeepSocial.py john_doe --c sm
```

## Contributing
Feel free to fork the repository and submit pull requests. Any suggestions or improvements are welcome.


