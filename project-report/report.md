# Manage Files Across Cloud Providers :hand: fa18-516-18

| Richa Rastogi
| rirastog@iu.edu
| Indiana University
| hid: fa18-516-18
| github: [:cloud:](https://github.com/cloudmesh-community/fa18-516-18/blob/master/project-paper/report.md)

---

Keywords: Multi-cloud data service, Cloud Computing, Python, Open API, Cloud Providers, MongoDB, Swagger

---

## Abstract

The goal of this project is to manage files across different cloud providers. There are many cloud providers where we can store data like AWS, Azure, google, etc. Here we are going to build an OpenAPI to manage these files, operations like copy, upload or download from one location/provider to another. 


## Introduction

The objective of this project is to manage data across different cloud providers. We are going to build an Open API for managing the data between all the cloud storages. We will analyse how these different clouds work and then build python methods to handle data across them. Final step will be to expose these functionalities as an API.

## Design

## Architecture

OpenAPI specification for copy function
	Boolean isFileCopied = copyFile({name of the file}, {source cloud provider}, {destination cloud provider}) 
	
Similarly we can have API for other functionalities as well. We can also split verification into a separate API because this might be commonly used across all functionalities.

## Dataset

## Implementation

## Benchmark

## Conclusion

## Acknowledgement

## References