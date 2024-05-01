from setuptools import setup, find_packages

print('Found packages:', find_packages())
setup(
    description='HaMeR as a package',
    name='hamer',
    packages=find_packages(),
    install_requires=[
        'gdown',
        'numpy',
        'opencv-python',
        'pyrender',
        'scikit-image>=0.21.0',
        'smplx==0.1.28',
        'yacs',
        'detectron2 @ git+https://github.com/facebookresearch/detectron2.git@a59f05630a8f205756064244bf5beb8661f96180',
        'chumpy @ git+https://github.com/mattloper/chumpy',
        'timm',
        'einops',
        'xtcocotools',
        'pandas',
    ],
    extras_require={
        'all': [
            'hydra-core',
            'hydra-submitit-launcher',
            'hydra-colorlog',
            'pyrootutils',
            'rich',
            'webdataset',
        ],
    },
)
