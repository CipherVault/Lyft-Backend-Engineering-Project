from datetime import datetime
from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
    
    @abstractmethod
    def engine_should_be_serviced(self):
        pass
    
    def needs_service(self, years_threshold=4, mileage_threshold=60000):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + years_threshold)
        return service_threshold_date < datetime.today().date() or self.engine_should_be_serviced(mileage_threshold)

class CapuletEngine(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
    
    def engine_should_be_serviced(self, mileage_threshold=30000):
        return self.current_mileage - self.last_service_mileage > mileage_threshold

class SternmanEngine(Car):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on
    
    def engine_should_be_serviced(self, mileage_threshold=None):
        return self.warning_light_is_on

class WilloughbyEngine(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
    
    def engine_should_be_serviced(self, mileage_threshold=60000):
        return self.current_mileage - self.last_service_mileage > mileage_threshold