from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from cart.cart import Cart
from .serializers import CartAddSerializer
from products.models.products import Product


class CartAddGenericApiView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = CartAddSerializer

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            product_id = serializer.validated_data["product_id"]
            quantity = serializer.validated_data["quantity"]

            product = Product.objects.get(id=product_id)

            cart = Cart(request.user.id)
            cart.add(
                product_id=product_id,
                quantity=quantity,
                price=product.price,
            )
            return Response(
                {"detail": "product added to cart"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart = Cart(request.user.id)
        return Response(
            {
                "items": cart.cart,
                "total_price": cart.get_total_price(),
                "total_items": len(cart),
            }
        )


class CartRemoveApiView(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request, product_id):
        cart = Cart(request.user.id)

        if str(product_id) not in cart.cart:
            return Response(
                {"detail": "product not in cart"}, status=status.HTTP_404_NOT_FOUND
            )

        cart.remove(product_id)
        return Response({"detail": "item removed from your cart"})


class ClearCartApiView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        cart = Cart(request.user.id)

        cart.clear()

        return Response({"detail": "cart cleared"})
