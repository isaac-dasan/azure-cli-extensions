# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class ActionStatusEnum(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Describes whether the order item is deletable or not.
    """

    ALLOWED = "Allowed"  #: Allowed flag.
    NOT_ALLOWED = "NotAllowed"  #: Not Allowed flag.

class ActionType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs.
    """

    INTERNAL = "Internal"

class AddressType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of address.
    """

    NONE = "None"  #: Address type not known.
    RESIDENTIAL = "Residential"  #: Residential Address.
    COMMERCIAL = "Commercial"  #: Commercial Address.

class AddressValidationStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Status of address validation
    """

    VALID = "Valid"  #: Address provided is valid.
    INVALID = "Invalid"  #: Address provided is invalid or not supported.
    AMBIGUOUS = "Ambiguous"  #: Address provided is ambiguous, please choose one of the alternate addresses returned.

class AvailabilityStage(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Current availability stage of the product. Availability stage
    """

    AVAILABLE = "Available"  #: Product is available.
    COMING_SOON = "ComingSoon"  #: Product is coming soon.
    PREVIEW = "Preview"  #: Product is in preview.
    DEPRECATED = "Deprecated"  #: Product is deprecated.
    SIGNUP = "Signup"  #: Product is available only on signup.
    UNAVAILABLE = "Unavailable"  #: Product is not available.

class BillingType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Represents billing type.
    """

    PAV2 = "Pav2"  #: PaV2 billing.
    PURCHASE = "Purchase"  #: Purchase billing.

class ChargingType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Charging type.
    """

    PER_ORDER = "PerOrder"  #: Per order charging type.
    PER_DEVICE = "PerDevice"  #: Per device charging type.

class CreatedByType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class DescriptionType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of description.
    """

    BASE = "Base"  #: Base description.

class DisabledReason(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Reason why the product is disabled.
    """

    NONE = "None"  #: Not disabled.
    COUNTRY = "Country"  #: Not available in the requested country.
    REGION = "Region"  #: Not available to push data to the requested Azure region.
    FEATURE = "Feature"  #: Required features are not enabled.
    OFFER_TYPE = "OfferType"  #: Subscription does not have required offer types.
    NO_SUBSCRIPTION_INFO = "NoSubscriptionInfo"  #: Subscription has not registered to Microsoft.DataBox and Service does not have the subscription notification.
    NOT_AVAILABLE = "NotAvailable"  #: The product is not yet available.
    OUT_OF_STOCK = "OutOfStock"  #: The product is out of stock.

class DoubleEncryptionStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Double encryption status as entered by the customer. It is compulsory to give this parameter if
    the 'Deny' or 'Disabled' policy is configured.
    """

    DISABLED = "Disabled"  #: Double encryption is disabled.
    ENABLED = "Enabled"  #: Double encryption is enabled.

class ImageType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the image
    """

    MAIN_IMAGE = "MainImage"  #: Main image.
    BULLET_IMAGE = "BulletImage"  #: Bullet image.
    GENERIC_IMAGE = "GenericImage"  #: Generic image.

class LengthHeightUnit(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Unit for the dimensions of length, height and width.
    """

    IN_ENUM = "IN"  #: Inch, applicable for West US.
    CM = "CM"  #: Centimeter.

class LinkType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of link
    """

    GENERIC = "Generic"  #: Generic link.
    TERMS_AND_CONDITIONS = "TermsAndConditions"  #: Terms and conditions link.
    SPECIFICATION = "Specification"  #: Link to product specification.
    DOCUMENTATION = "Documentation"  #: Link to product documentation.
    KNOW_MORE = "KnowMore"  #: Link to know more.
    SIGN_UP = "SignUp"  #: Link to sign up for products.

class MeteringType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Represents Metering type (eg one-time or recurrent)
    """

    ONE_TIME = "OneTime"  #: One time billing.
    RECURRING = "Recurring"  #: Recurring billing.
    ADHOC = "Adhoc"  #: Adhoc billing.

class NotificationStageName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Name of the stage.
    """

    SHIPPED = "Shipped"  #: Notification at order item shipped from microsoft datacenter.
    DELIVERED = "Delivered"  #: Notification at order item delivered to customer.

class OrderItemCancellationEnum(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Describes whether the order item is cancellable or not.
    """

    CANCELLABLE = "Cancellable"  #: Order item can be cancelled without fee.
    CANCELLABLE_WITH_FEE = "CancellableWithFee"  #: Order item can be cancelled with fee.
    NOT_CANCELLABLE = "NotCancellable"  #: Order item not cancellable.

class OrderItemReturnEnum(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Describes whether the order item is returnable or not.
    """

    RETURNABLE = "Returnable"  #: Order item can be returned without fee.
    RETURNABLE_WITH_FEE = "ReturnableWithFee"  #: Order item can be returned with fee.
    NOT_RETURNABLE = "NotReturnable"  #: Order item not returnable.

class OrderItemType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Order item type.
    """

    PURCHASE = "Purchase"  #: Purchase OrderItem.
    RENTAL = "Rental"  #: Rental OrderItem.

class Origin(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system"
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"

class StageName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Stage name
    """

    PLACED = "Placed"  #: Currently in draft mode and can still be cancelled.
    IN_REVIEW = "InReview"  #: Order is currently in draft mode and can still be cancelled.
    CONFIRMED = "Confirmed"  #: Order is confirmed.
    READY_TO_SHIP = "ReadyToShip"  #: Order is ready to ship.
    SHIPPED = "Shipped"  #: Order is in transit to customer.
    DELIVERED = "Delivered"  #: Order is delivered to customer.
    IN_USE = "InUse"  #: Order is in use at customer site.
    RETURN_INITIATED = "ReturnInitiated"  #: Return has been initiated by customer.
    RETURN_PICKED_UP = "ReturnPickedUp"  #: Order is in transit from customer to microsoft.
    RETURNED_TO_MICROSOFT = "ReturnedToMicrosoft"  #: Order has been received back to microsoft.
    RETURN_COMPLETED = "ReturnCompleted"  #: Return has now completed.
    CANCELLED = "Cancelled"  #: Order has been cancelled.

class StageStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Stage status.
    """

    NONE = "None"  #: No status available yet.
    IN_PROGRESS = "InProgress"  #: Stage is in progress.
    SUCCEEDED = "Succeeded"  #: Stage has succeeded.
    FAILED = "Failed"  #: Stage has failed.
    CANCELLED = "Cancelled"  #: Stage has been cancelled.
    CANCELLING = "Cancelling"  #: Stage is cancelling.

class SupportedFilterTypes(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of product filter.
    """

    SHIP_TO_COUNTRIES = "ShipToCountries"  #: Ship to country.
    DOUBLE_ENCRYPTION_STATUS = "DoubleEncryptionStatus"  #: Double encryption status.

class TransportShipmentTypes(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates Shipment Logistics type that the customer preferred.
    """

    CUSTOMER_MANAGED = "CustomerManaged"  #: Shipment Logistics is handled by the customer.
    MICROSOFT_MANAGED = "MicrosoftManaged"  #: Shipment Logistics is handled by Microsoft.

class WeightMeasurementUnit(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Unit for the dimensions of weight.
    """

    LBS = "LBS"  #: Pounds.
    KGS = "KGS"  #: Kilograms.