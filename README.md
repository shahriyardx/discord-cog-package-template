# Discord cog package
The long description about the package

### Usage 
- Clone this repository and change folder name of `package` to the name you want on pypi, it will also be the `load_extension('name')`
- Modify the cog and setup.py with required info. 
    - The name in setup.py can be different from package name, that name will be used to install the package not to load if thats different.
    - Change the required python version for your package.
- Build the package using the commands
    - python setup.py sdist
- Upload it to pypi
    - Register on pypi
    - install twine `pip install twine`
    - Upload command `twine upload --skip-existing`
    - Then it will ask for your pypi username ans password

After everything done anyone can install your pypi lib and use it in their bot. By loading it using `bot.load_extension('package_name')`

For help [Join Discord](https://discord.gg/7SaE8v2)