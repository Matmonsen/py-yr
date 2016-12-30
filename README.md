# py-yr

### Installation
```bash
pip install git+git://github.com/Matmonsen/py-yr.git#egg=py-yr
```
### Usage
```python
from py_yr.yr import Yr

yr = Yr("Norway/Hordaland/Bergen/Bergen/", "en", "standard")
yr.download()


# Get weather data in different formats

# Returns a nested dict with weather data
yr.get_as_dict()

# Returns the original weather data
yr.get_as_xml() # same as yr.source_data

# Returns an WeatherData object containing the forecast
yr.get_as_object()
```

### [License](https://github.com/Matmonsen/py-yr/blob/master/LICENSE)

### See also
 [Repository with css web font for yr weather symbols](https://github.com/Matmonsen/yr-icons/)

