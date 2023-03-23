from setuptools import find_packages, setup


HYPHEN_E_DOT: str = "-e ."

def get_rquirements(file_path: str) -> list[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as f_obj:
        requirements = f_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Subhranil',
    author_email='subhranil.sarkar2605@gmail.com',
    packages=find_packages(),
    install_requires=get_rquirements('requirements.txt')
)